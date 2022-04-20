import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from Zaid.filters import command
from Zaid.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
✦ Hello, My name is Ankit & Khushi Music bot.I'm a telegram streaming bot with some useful features.
┏━━━━━━━━━━━━━━━━━┓
┣✦ Developer : [⇆](https://t.me/ANKIT_KHUSHI)
┣✦ Support   : [◁](https://t.me/Blaze_Support)
┣✦ About Me  : [❚❚](t.me/ITZZ_OFFICIAL)
┣✦ Updates   : [▷](https://t.me/LOVE_X_POISONS)
┣✦ ChiChat   : [↻](https://t.me/UNIQUE_SOCIETY)
┗━━━━━━━━━━━━━━━━━┛ 
✦ POWERED BY- [ANKIT AND KHUSHI](https://t.me/Official_Afk_xD) .
▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add Ankit & Khushi To Your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✦ Support", url=f"T.ME/TheMafiaSupport"
                    ),
                    InlineKeyboardButton(
                        "Updates ✦", url=f"t.me/TheMafiaNetwork"
                    )                               
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6d01c63f9ed44610d6b1d.jpg",
        caption=f"""✦ Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✦ Join Here And Support ✦", url=f"https://t.me/{GROUP_SUPPORT}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6d01c63f9ed44610d6b1d.jpg",
        caption=f"""✦ Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✦ Source Code ✦", url=f"https://github.com/Official-afk-xD/Lovely-Robot")
                ]
            ]
        ),
    )
