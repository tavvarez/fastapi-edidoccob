from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from dotenv import load_dotenv;
import os;

load_dotenv(override=True);

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL);
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine);

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()