from fastapi import APIRouter, Request
from app.services.telegram_service import process_telegram_update

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await process_telegram_update(update)
    return {"status": "ok"}