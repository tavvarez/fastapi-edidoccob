from fastapi import FastAPI
from app.api.v1.endpoints import upload, user_input, edi, download_edi

app = FastAPI(title="fastapi-edibialog", swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})
app.include_router(upload.router, prefix="/api/v1")
app.include_router(user_input.router, prefix="/api/v1")
app.include_router(edi.router, prefix="/api/v1")
app.include_router(download_edi.router, prefix="/api/v1")