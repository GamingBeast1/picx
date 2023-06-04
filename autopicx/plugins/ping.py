#© 𝙄𝙩𝙨 ⚡ 𝙅𝙤𝙚𝙡 | #𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆

from .. import client
from telethon import events
import logging 
import asyncio
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -- Constants -- #
HELP = "**✨ Plugins ✨**\n\n`!start` - __To Start Changing DP__\n`!cancel` - __To Cancel Changing DP__\n`!alive` - __To Check If Bot Is Alive__\n`!repo` - __To Get The Repo__\n`!about` - __Details About Me__\n`!help` - __For This Message__"

ABOUT_TXT = """
᪥ **Name:** 𝘼𝙪𝙩𝙤𝙋𝙞𝙘𝙓
᪥ **Library: [Telethon](https://docs.telethon.dev/)**
᪥ **Language: [Python 3](https://www.python.org)**
᪥ **Dev:** [𝙄𝙩𝙨 ⚡ 𝙅𝙤𝙚𝙡](https://t.me/joel_noob)
᪥ **Inspiration: [Dᴋ 🇮🇳](https://t.me/AbOutMe_DK)**
"""

REPO = "https://github.com/git-itsjoel/AutoPicX"

@client.on(events.NewMessage(outgoing=True, pattern='!repo'))
async def repo(event):
    await event.edit(REPO, link_preview=False)

@client.on(events.NewMessage(outgoing=True, pattern='!about'))
async def about(event):
    await event.edit(ABOUT_TXT, link_preview=False)


@client.on(events.NewMessage(outgoing=True, pattern='!help'))
async def help_me(event):
    await event.edit(HELP)


@client.on(events.NewMessage(outgoing=True, pattern='!alive'))
async def alive(event):
    txt = await event.edit("▢▢▢")
    await event.edit("▣▢▢")
    await event.edit("▣▣▢")
    await event.edit("▣▣▣")
    await event.edit("𝘼𝙪𝙩𝙤𝙋𝙞𝙘𝙓 𝙄𝙨 𝘼𝙘𝙩𝙞𝙫𝙚")
