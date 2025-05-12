from typing import List
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends;
from sqlalchemy.orm import Session;
from app.services.xml_parser import parse_cte_xml;
from app.models.cte import CteInfo;
from app.core.database import get_db;

router = APIRouter();
@router.post("/upload-xml")
async def upload_xml(files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    cte_ids = []
    for file in files:
        if not file.filename.endswith('.xml'):
            raise HTTPException(status_code=400, detail=f"Tipo de arquivo inválido. Apenas XML é permitido. {file.filename}")
        try:
            contents = await file.read()
            temp_path = f"/tmp/{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(contents)

            dados = parse_cte_xml(temp_path)
            novo_cte = CteInfo(**dados)
            db.add(novo_cte)
            db.flush()
            cte_ids.append(novo_cte.id)
            db.refresh(novo_cte)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao processar {file.filename}: {str(e)}")
    
    db.commit()
    return {"message": f"{len(cte_ids)} XMLs processados e salvos", "cte_ids": cte_ids}