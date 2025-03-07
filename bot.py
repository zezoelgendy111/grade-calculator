import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
import requests

TOKEN = "8064058184:AAGKrCFHW9d0rHaJbbeqDlnRTFNVV2omM6Y"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# زر لفتح WebApp داخل تيليجرام
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚀 فتح الحاسبة", web_app=WebAppInfo(url="https://yourwebsite.com/index.html"))]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("مرحبًا! 😊 استخدم الزر أدناه لفتح حاسبة التقدير:", reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
