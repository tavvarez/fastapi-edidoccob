from fastapi import APIRouter, UploadFile, File, HTTPException, Depends;
from sqlalchemy.orm import Session;
from app.services.xml_parser import parse_cte_xml;
from app.models.cte import CteInfo;
from app.core.database import get_db;

router = APIRouter();
@router.post("/upload-xml")
async def upload_xml(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.xml'):
        raise HTTPException(status_code=400, detail="Tipo de arquivo inválido. Apenas XML é permitido.");
    try:
        contents = await file.read();
        with open(f"/tmp/{file.filename}", "wb") as f:
            f.write(contents);

        dados = parse_cte_xml(f"/tmp/{file.filename}");
        novo_cte = CteInfo(**dados);
        db.add(novo_cte);
        db.commit();
        db.refresh(novo_cte);
        return {"message": "XML processado e salvo", "cte_id": novo_cte.id};
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e));