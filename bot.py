import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Головні кнопки
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="кузя")],
        [KeyboardButton(text="цветочки")]
    ],
    resize_keyboard=True
)

# Меню після натискання на "кузя"
kuzya_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="еда"), KeyboardButton(text="уборка")],
        [KeyboardButton(text="назад")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Обирай:", reply_markup=main_keyboard)

@dp.message(F.text == "назад")
async def back_handler(message: Message):
    await message.answer("Меню:", reply_markup=main_keyboard)

# Натискаємо на "кузя"
@dp.message(F.text == "кузя")
async def kuzya_handler(message: Message):
    await message.answer("Кузя:", reply_markup=kuzya_keyboard)

# Кнопка "еда"
@dp.message(F.text == "еда")
async def food_handler(message: Message):
    text = (
        "🟢 ЩО ТРЕБА ДАВАТИ ЗАРАЗ \n"
        "Сухе сіно -- ГОЛОВНЕ\n"
        "Трава\n"
        "огіркі\n"
        "кабачкі\n"
        "болгарській перец\n"
        "зелень\n\n"
        "🔴 ЩО НЕ МОЖНА ДАВАТИ ЗАРАЗ (Під забороною через вагу та шлунок) але можно чучуть\n"
        "капуста\n"
        "морковка та буряк\n"
        "яблука груши банани\n"
        "хліб сухарі печево"
    )
    await message.answer(text)

# Кнопка "уборка"
@dp.message(F.text == "уборка")
async def cleaning_handler(message: Message):
    text = (
        "УБОРКА\n"
        "дастайом кузу патом забераєм пельонку \n"
        "викідуєм\n"
        "меняєм верхнію пельонку гамака\n"
        "застеляєм новою і ложим вещі\n"
        "насепаєм корм\n"
        "меняєм воду\n"
        "єслі пельонкі закончелісь то іх надо порезать\n"
        "інструкция ніже"
    )
    await message.answer(text)
    
    # Відправка фото
    photo = FSInputFile("pelionka.jpg")
    await message.answer_photo(photo=photo)

# Кнопка "цветочки"
@dp.message(F.text == "цветочки")
async def flowers_handler(message: Message):
    await message.answer("цветочки")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
