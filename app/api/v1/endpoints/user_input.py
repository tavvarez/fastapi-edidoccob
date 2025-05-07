from fastapi import APIRouter, Depends, HTTPException;
from sqlalchemy.orm import Session;
from app.core.database import get_db;
from app.models.user_input import UserInput;
from app.schemas.user_input_schema import UserInputCreate, UserInputOut;

router = APIRouter();

@router.post("/", response_model=UserInputOut)
def create_user_input(data: UserInputCreate, db: Session = Depends(get_db)):
    try:
        novo = UserInput(**data.dict());
        db.add(novo);
        db.commit();
        db.refresh(novo);
        return novo;
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e));