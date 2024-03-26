import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("oggy", CMD))
async def check_alive(_, message):
    await message.reply_text("🥹🫂")
