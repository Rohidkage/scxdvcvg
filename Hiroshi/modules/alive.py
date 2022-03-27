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
  GREY = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Turbo Robot.** \n\n"
  GREY += "⚪ **I'm Working Properly** \n\n"
  GREY += f"⚪ **My Master : [Hiro](https://t.me/Bisuinhiro)** \n\n"
  GREY += f"⚪ **Library Version :** `{telever}` \n\n"
  GREY += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  GREY += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  GREY += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/TurboHiroBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/hiroshisupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=HIROSHI,  buttons=BUTTON)
