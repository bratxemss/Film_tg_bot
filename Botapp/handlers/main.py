import asyncio
import re

from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

# from .utils import ()


@Client.on_message(filters.command("help", ["/", ".", "?"]))
async def helper(client, message):
    markup = ReplyKeyboardMarkup(
        [
            [KeyboardButton("Chose language of searching")],
            [KeyboardButton("Find film info")],
            [KeyboardButton("Get recommendations")]
        ],
        resize_keyboard=True
    )
    asyncio.ensure_future(
        client.send_message(
            message.from_user.id,
            text=f"Hello, {message.from_user.first_name}! I am Movie Station. I will send you information about you "
            f"favorite films!",
            reply_markup=markup
        )
    )
    return


@Client.on_message(
    filters.text &
    (
            filters.regex(re.compile(r"^Chose language of searching$"))
            | filters.regex(re.compile(r"^Find film info$"))
            | filters.regex(re.compile(r"^Get recommendations$"))

    ),
    group=1)
async def process_operations(client, message):
    if message.text == "Chose language of searching":
        await client.send_message()
        #do select for user
    elif message.text == "Find film info":
        await client.send_message()
    elif message.text == "Get recommendations":
        await client.send_message()
    return
