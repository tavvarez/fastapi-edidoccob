import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.edi_generated import EDIGenerated

router = APIRouter()

@router.get("/edi/download/{user_input_id}", response_class=FileResponse)
def download_edi(user_input_id: int, db: Session = Depends(get_db)):
    edi = db.query(EDIGenerated).filter_by(user_input_id=user_input_id).first()
    if not edi or not os.path.exists(edi.caminho_arquivo):
        raise HTTPException(status_code=404, detail="Arquivo EDI não encontrado.")
    
    return FileResponse(
        path=edi.caminho_arquivo,
        media_type='text/plain',
        filename=os.path.basename(edi.caminho_arquivo)
    )