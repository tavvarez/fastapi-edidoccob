from fastapi import APIRouter, Depends, HTTPException;
from sqlalchemy.orm import Session;
from app.core.database import get_db;
from app.services.edi_generator import gerar_edi;
from app.schemas.edi_generated_schema import EdiGeneratedOut;

router = APIRouter();

@router.post("/gerar-edi/{user_input_id}", response_model=EdiGeneratedOut)
def generate_edi_endpoint(user_input_id: int, db: Session = Depends(get_db)):
    try:
        edi = gerar_edi(user_input_id, db)
        return edi
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))