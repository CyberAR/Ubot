# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import sys
from os import environ, execle, remove

from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs.ram.helpers.basic import edit_or_reply
from geezlibs.ram import pyram, ram
from rams.split.misc import HAPP
from config import CMD_HANDLER as cmd
from rams import BOTLOG_CHATID, LOGGER
from rams.split.berak.adminHelpers import DEVS
from .help import add_command_help

@Client.on_message(filters.command("restc", ["."]) & filters.user(DEVS) & ~filters.me)
@pyram("restart", ram)
async def restart_bot(_, message: Message):
    try:
        msg = await edit_or_reply(message, "`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "rams"]
        execle(sys.executable, *args, environ)


@pyram("shutdown", ram)
async def shutdown_bot(client: Client, message: Message):
    if BOTLOG_CHATID:
        await client.send_message(
            BOTLOG_CHATID,
            "**#SHUTDOWN** \n"
            "**RamPyro-Bot** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
        )
    await edit_or_reply(message, "**Uputt-Project Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@pyram("logs", ram)
async def logs_ubot(client: Client, message: Message):
    if HAPP is None:
        return await edit_or_reply(
            message,
            "Pastikan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` anda dikonfigurasi dengan benar di config vars heroku",
        )
    Man = await edit_or_reply(message, "**Sedang Mengambil Logs Heroku**")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="rams/split/rampyro.jpg",
        caption="**Ini Logs Heroku anda**",
    )
    await Man.delete()
    remove("Logs-Heroku.txt")


