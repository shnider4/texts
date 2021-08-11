from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.raw.types import UpdateNewMessage

from mongodb.channels import add_channel_to_db, remove_channel_from_db, channel_list
from mongodb.users import user_list
from mongodb.users import add_client_to_db

from sample_config import Config

import logging
from os import walk
from __banner.banner import bannerTop
from mongodb.channels import channel_list

banner = bannerTop()
logging.info("\n{}".format(banner))


@Client.on_message(filters.private & filters.command("sbs") & filters.user(Config.owner_id))
async def sbs_bot(Client, message):
    chats = await user_list()
    sbs = len(chats)
    await message.reply(
        f"الاحصائيات : \n\n عدد المشتركين في البوت  {sbs}"

    )


@Client.on_message(filters.private & filters.command("chlist") & filters.user(Config.owner_id))
async def forc_ch(Client, message):
    forc_ch = await channel_list()
    forc_ch = len(forc_ch)
    await message.reply(
        f"الاحصائيات : \n\n عدد المشتركين في البوت  {forc_ch}"

    )


@Client.on_message(filters.private & filters.command("broadcast") & filters.user(Config.owner_id))
async def broadcast(client, message):
    to_send = message.reply_to_message.text
    print(to_send)
    chats = await user_list()
    success = 0
    failed = 0
    for chat in chats:

        try:
            await client.send_message(int(chat), to_send)

            success += 1
        except:
            failed += 1
            # remove_chat_from_db(str(chat))
            pass
    await message.reply(
        f"Message sent to {success} chat(s). {failed} chat(s) failed recieve message"
    )


@Client.on_message(filters.private & filters.command('set') & filters.user(Config.owner_id))
async def set_chat(client, message):
    channel = message.reply_to_message.forward_from_chat
    title = channel["title"]
    username = channel["username"]
    channel_id = channel["id"]
    await add_channel_to_db(channel_id)
    print(channel)
    channels = await channel_list()
    channels = len(channels)

    await message.reply(
        f" تم اضافة القناة في الاشتراك الاجباري \n\n اسم القناة : {title} \nمعرف القناة : {username} \n عدد قنوات الاشتراك الاجباري الحالية {channels}\n")


@Client.on_message(filters.private & filters.command("delset") & filters.user(Config.owner_id))
async def delset_chat(client, message):
    channel_id = message.reply_to_message.forward_from_chat.id
    print(channel_id)
    await remove_channel_from_db(channel_id)
    await message.reply(
        "تمم "

    )


@Client.on_message(filters.private & filters.command("cler") & filters.user(Config.owner_id))
async def cler_chat(client, message):
    all = await channel_list()
    chats = len(all)
    print(chats)
    for chat in all:
        print(chat)
        await remove_channel_from_db(chat)


owner_help = """

/broadcast اذاعة
/sbs مشتركين البوت
/set تعين اشتراك اجباري
/delset الغاء  تعين اشتراك اجباري
"""


@Client.on_message(filters.private & filters.command("start") & filters.user(Config.owner_id))
async def start(client, message):
    add_status, total_users = await add_client_to_db(
        message.from_user.id
    )
    if add_status == 1:
        await Client.send_message(
            chat_id=Config.owner_id,
            text="🆕 مشترك جديد في البوت!\nTotal: {}\nName: {}\nUsername: @{}".format(
                total_users, message.from_user.first_name, message.from_user.username
            ),
            disable_notification=True,
        )
    await message.reply(owner_help)
