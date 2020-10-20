# TAKEN FROM CRACKBOT
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "CrackBot"
PM_IMG = "https://telegra.ph/file/266ddfc9ee87c53cf445b.jpg"
pm_caption = "**ᴘɪᴋᴀᴄʜᴜ ɪs ᴏɴʟɪɴᴇ**\n\n"
pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** : 15.0.0\n"
pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** : [ᴊᴏɪɴ](https://t.me/PROJECT_PIKACHU)\n"
pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ** : [ᴛᴇᴀᴍ ᴘɪᴋᴀᴄʜᴜ](https://github.com/TEAM-PIKACHU-INDIA/PIKACHU-THE-USERBOT)\n"
pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** : [ᴛᴇᴀᴍ ᴘɪᴋᴀᴄʜᴜ](https://github.com/TEAM-PIKACHU-INDIA)\n\n"
pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** : {DEFAULTUSER}\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
