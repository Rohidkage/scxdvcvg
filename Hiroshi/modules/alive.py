import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Hiroshi.events import register
from Hiroshi import telethn as tbot


PHOTO = "https://telegra.ph/file/b3329dd79719e54ba334f.mp4"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), Saya Adalah HiroshiRobot.** \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += "➥ **I'm Working Properly** \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += f"➥ **My Master : [нιяσѕнι ꭙ ᴅᴇᴠᴇʟᴏᴘᴇʀ ](https://t.me/splesneey)** \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += f"➥ **Library Version :** `{telever}` \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += f"➥ **Telethon Version :** `{tlhver}` \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += f"➥ **Pyrogram Version :** `{pyrover}` \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("👮‍♂️ 𝙱ᴀɴᴛᴜᴀɴ​", "https://t.me/hiroshirobot?start=help"), Button.url("💌 𝙲ʜᴀɴɴᴇʟ​", "https://t.me/vailedcode")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=GREY,  buttons=BUTTON)
