import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/00f47c54ceda3944dc47c.jpg"
pm_caption = "**🔥ᴘɪᴋᴀᴄʜᴜ ɪs ᴏɴʟɪɴᴇ❤**\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"

pm_caption += "ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ        :  15.0.0 \n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/)\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        : [ᴊᴏɪɴ](https://t.me/)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ                 : [ʟɪᴄᴇɴꜱᴇ](https://github.com/TEAM-PIKACHU-INDIA/PIKACHU-THE-USERBOT/blob/master/LICENSE)\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ             : [ᴛᴇᴀᴍ ᴘɪᴋᴀᴄʜᴜ](https://github.com/team-pikachu-india)\n"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
