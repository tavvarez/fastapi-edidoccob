from fastapi import FastAPI;
from app.api.v1.endpoints import upload;

app = FastAPI(title="fastapi-edibialog");
app.include_router(upload.router, prefix="/api/v1");