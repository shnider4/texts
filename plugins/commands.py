
# المطور ,,,,, t.me/shnider_bots
import json

import requests
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.raw.types import UpdateNewMessage

from mongodb.channels import add_channel_to_db, remove_channel_from_db, channel_list
from mongodb.users import user_list, remove_client_from_db
from mongodb.users import add_client_to_db
from mongodb.members import *
from plugins.fonts import Fonts

from sample_config import Config

import logging
from os import walk
from __banner.banner import bannerTop
from mongodb.channels import channel_list

banner = bannerTop()
logging.info("\n{}".format(banner))

@Client.on_message(filters.private & filters.command("start"))
async def startt_bot(Client, message):
    userid = str(message.from_user.id)
    owner_id = str(Config.owner_id)
    update_channel = await  channel_list()
    chats = await members_list()
    add_status, total_users = await add_client_to_db(
        message.from_user.id
    )
    if add_status == 1:
        await client.send_message(
            chat_id=Config.owner_id,
            text="🆕 مشترك جديد في البوت!\nTotal: {}\nName: {}\nUsername: @{}".format(
                total_users, message.from_user.first_name, message.from_user.username
            ),
            disable_notification=True,
        )

    if userid == owner_id:
        await message.reply_text(owner_help)
    elif userid in chats:
        await message.reply_text("ارسل اسمك  لزغرفتة بالسومرية مثل \n `احمد : 𒅈𒍣` \n `زينب : 𒈨𒈠𒀭 ` ")

    else:
        for update_channel in update_channel:
            link = f"https://t.me/{update_channel}"

            print("no")
            await message.reply_text(
                f"🚸| عذرا عزيزي \n🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه\n\n - {link} \n\n ‼️| اشترك ثم ارسل /start ",
                disable_web_page_preview=True)
            await add_members_to_db(userid)


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
            await remove_client_from_db(str(chat))
            pass
    print(failed)
    await message.reply(
        f" تم إرسال الرسالة إلى {success}  من الاشخاص.\n\n  {failed}  من الاشخاص فشل في تلقي الرسالة "
    )
    if failed > 0:
        await message.reply(f"تم حذف المحظورين {failed} من قاعدة البيانات  ")


@Client.on_message(filters.private & filters.command('set') & filters.user(Config.owner_id))
async def set_chat(client, message):
    channel = message.reply_to_message.forward_from_chat
    title = channel["title"]
    username = channel["username"]
    channel_id = username
    await add_channel_to_db(channel_id)
    print(channel)
    channels = await channel_list()
    channels = len(channels)

    await message.reply(
        f"👨🏼‍💻| تم اضافة القناة في الاشتراك الاجباري \n\n🔐 اسم القناة : {title} \n🆔 معرف القناة : @{username} \n🌐عدد قنوات الاشتراك الاجباري الحالية  {channels}\n")


@Client.on_message(filters.private & filters.command("delset") & filters.user(Config.owner_id))
async def delset_chat(client, message):
    channel_id = message.reply_to_message.forward_from_chat.id
    print(channel_id)
    await remove_channel_from_db(channel_id)
    await message.reply(
        "تمم "

    )


@Client.on_message(filters.private & filters.command("cler") & filters.user(Config.owner_id)& filters.incoming)
async def cler_chat(client, message):
    all = await channel_list()
    chats = len(all)
    print(chats)
    for chat in all:
        print(chat)
        await remove_channel_from_db(chat)
    await message.reply(
            "تم حذف جميع قنوات الاشتراك الاجباري 🗑 📭 "

        )


owner_help = """

/broadcast اذاعة
/sbs مشتركين البوت
/set تعين اشتراك اجباري
/cler  حذف جميع قنوات الاشتراك الاجباري  
/delset الغاء  تعين اشتراك اجباري
/member
"""



@Client.on_message(filters.private & filters.command("member") & filters.user(Config.owner_id))
async def cler_member(client, message):
    all = await members_list()
    chats = len(all)
    print(chats)
    for chat in all:
        print(chat)
        await remove_members_from_db(chat)
    await message.reply(
            "تم حذف جميعاعضاءالاشتراك الاجباري 🗑 📭 "

        )
