import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# 1. Твой токен от @BotFather
BOT_TOKEN = "8952674443:AAHaBDmBR7uv8Aeww0b-DEzgl8vyjx4QylU"

# 2. Ссылка на твой профиль Roblox
ROBLOX_URL = "https://roblox.com.ms/users/266872929/profile"

dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message):
    # Создаём кнопку со ссылкой
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎮 Мой Roblox профиль", url=ROBLOX_URL)]
        ]
    )

    text = (
        f"Привет, {message.from_user.first_name}!\n\n"
        f"Хочешь получить бесплатных петов?! Добавь меня в друзья по сыллку каждому я напишу в лс и выдам петов\n"
        f"Вот ссылка на мой Roblox профиль: {ROBLOX_URL}\n"
        f"Добавьте меня в друзья! 🤝"
    )

    await message.answer(text, reply_markup=keyboard)

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())