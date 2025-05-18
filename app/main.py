from fastapi import FastAPI
from app.api.endpoints import telegram

app = FastAPI(title="Azərbaycan Dili Botu")

app.include_router(telegram.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Azərbaycan Dili Botu API"}