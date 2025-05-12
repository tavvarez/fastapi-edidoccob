# edi_generator.py (orquestrador)
import os
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user_input_cte_link import UserInputCTELink
from app.models.cte import CteInfo
from app.models.user_input import UserInput
from app.models.edi_generated import EDIGenerated
from app.services.edi_builder import build_registros

EDI_DIR = "app/generated/edi"
os.makedirs(EDI_DIR, exist_ok=True)

def gerar_edi(user_input_id: int, db: Session):
    user_input = db.query(UserInput).filter(UserInput.id == user_input_id).first()
    if not user_input:
        raise ValueError("User input não encontrado")

    # ctes = db.query(CteInfo).filter(CteInfo.numero_cte == user_input.numero_cte).all()
    cte_ids = db.query(UserInputCTELink.cte_info_id).filter_by(user_input_id=user_input.id).all()
    cte_ids = [id for (id,) in cte_ids]
    ctes = db.query(CteInfo).filter(CteInfo.id.in_(cte_ids)).all()
    if not ctes:
        raise ValueError("CTE correspondente não encontrado")

    data = datetime.now()
    nome_arquivo = f"DOCCOB_{user_input.numero_fatura.replace(' ', '_')}_{data.strftime('%Y%m%d_%H%M%S')}.txt"
    caminho_completo = os.path.join(EDI_DIR, nome_arquivo)

    registros = build_registros(user_input, ctes)
    conteudo = "\n".join(registros)

    with open(caminho_completo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    
    novo_registro = EDIGenerated(
        nome_cliente=user_input.nome_cliente,
        caminho_arquivo=caminho_completo,
        user_input_id=user_input.id
    )
    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)
    return novo_registro
