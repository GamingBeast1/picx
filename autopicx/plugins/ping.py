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
HELP = """
𝙋𝙞𝙘𝙓 __Commands__

`!start` - __To Start Changing DP__
`!cancel` - __To Cancel Changing DP__
`!alive` - __To Check If Bot Is Alive__
`!repo` - __To Get The Repo__
`!about` - __Details About Me__
`!help` - __For This Message__
`!hype` - __To send abusive words__
`!gay` - __To send gay message__
"""

ABOUT_TXT = """
᪥ **Name:** Id manager bot
᪥ **Library: [Telethon](https://docs.telethon.dev/)**
᪥ **Language: [Python 3](https://www.python.org)**
᪥ **Dev:** [Ekampreet Singh](https://t.me/EK4mpreetsingh)
"""

REPO = """
𝙋𝙞𝙘𝙓 __is not an Open Source UserBot based on Telethon you can access it's source code from **[here](https://t.me/Ek4mpreetSingh)**__
"""

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
    await event.edit("(～￣▽￣)～")
    await event.edit("Bot is active")


@client.on(events.NewMessage(outgoing=True, pattern='!hype'))
async def alive(event):
    txt = await event.edit("▢▢▢")
    await event.edit("▣▢▢")
    await event.edit("▣▣▢")
    await event.edit("▣▣▣")
    await event.edit("Teri maa ki choot gand kay tatto teri maa ka bhosda karke uski gaand mai ping pong kar dunga

                     
@client.on(events.NewMessage(outgoing=True, pattern='!gay'))
async def alive(event):
    txt = await event.edit("You")
    await event.edit("are")
    await event.edit("gay🏳️‍🌈🏳️‍🌈")
