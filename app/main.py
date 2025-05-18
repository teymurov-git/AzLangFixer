from fastapi import FastAPI
from aiogram import Bot
from app.config.settings import settings

app = FastAPI(title="Azərbaycan Dili Botu")

@app.on_event("startup")
async def on_startup():
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    webhook_url = "https://127.0.0.1:8000/api/webhook"
    await bot.set_webhook(webhook_url)
    print(f"Webhook quruldu: {webhook_url}")

@app.get("/")
async def root():
    return {"message": "Azərbaycan Dili Botu API"}