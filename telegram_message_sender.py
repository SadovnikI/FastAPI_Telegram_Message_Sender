from fastapi import FastAPI, HTTPException
from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import TelegramError
from schemas import MessageData

app = FastAPI()


@app.post("/send_message")
async def send_message(data: MessageData):
    bot = Bot(token=data.bottoken)

    try:
        response = await bot.send_message(chat_id=data.chatid, text=data.message, parse_mode=ParseMode.HTML)
    except TelegramError as e:
        raise HTTPException(status_code=500, detail=f"Failed to send message to Telegram: {e}")

    return {"status": "Message sent successfully", "message_id": response.message_id}
