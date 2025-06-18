from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user_input import UserInput
from app.models.user_input_cte_link import UserInputCTELink
from app.schemas.user_input_schema import UserInputCreate, UserInputOut

router = APIRouter()

@router.post("/", response_model=UserInputOut)
def create_user_input(data: UserInputCreate, db: Session = Depends(get_db)):
    try:
        novo = UserInput(
            nome_cliente = data.nome_cliente,
            numero_fatura = data.numero_fatura,
            vencimento_fatura = data.vencimento_fatura
        )
        db.add(novo)
        db.flush()

        for cte_id in data.cte_ids:
            vinculo = UserInputCTELink(
                user_input_id = novo.id,
                cte_info_id = cte_id
        )
            db.add(vinculo)    

        db.commit()
        db.refresh(novo)
        return novo
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))