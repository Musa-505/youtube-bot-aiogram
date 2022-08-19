import os
from aiogram import *
from config import *
from pytube import YouTube

bot = Bot(Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Hello")

@dp.message_handler()
async def text_message(message:types.message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtube.com' or 'https://youtu.be':
        await bot.send_message(chat_id, "Start download :", parse_mode="Markdown")
        await download_youtube_vidio(url, message, bot)

async def download_youtube_vidio(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open (f'{message.chat.id}'/f'{message.chat.id}_{yt.title}', 'rb') as vidio:
        await bot.send_vidio(message.chat.id, vidio, caption="Bot stardet vidio +", parse_mode="Markdown")
        os.remove(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')


if __name__ == '__main__':
    executor.start_polling(dp)