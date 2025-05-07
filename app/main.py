from fastapi import FastAPI;
from app.api.v1.endpoints import upload, user_input;

app = FastAPI(title="fastapi-edibialog");
app.include_router(upload.router, prefix="/api/v1");
app.include_router(user_input.router, prefix="/api/v1");