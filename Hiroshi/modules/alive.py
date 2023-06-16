import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Hiroshi.events import register
from Hiroshi import telethn as tbot


PHOTO = "https://telegra.ph/file/909942858a15f63fbdefd.jpg"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), Saya Adalah KageRobot.** \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += "➥ **I'm Working Properly** \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += f"➥ **My Master : [нιяσѕнι ꭙ](https://t.me/kagebunshiiin)** \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += f"➥ **Library Version :** `{telever}` \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += f"➥ **Telethon Version :** `{tlhver}` \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += f"➥ **Pyrogram Version :** `{pyrover}` \n"
  GREY += f"➖➖➖➖➖➖➖➖\n"
  GREY += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("👮‍♂️ 𝙱ᴀɴᴛᴜᴀɴ​", "https://t.me/kagebunshiiin?start=help"), Button.url("💌 𝙲ʜᴀɴɴᴇʟ​", "https://t.me/kagestore69")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=GREY,  buttons=BUTTON)
