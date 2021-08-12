#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# المطور ,,,,, t.me/shnider_bots

import requests
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from mongodb.users import add_client_to_db
from .commands import start
from .fonts import Fonts
from mongodb.channels import channel_list

from sample_config import Config



async def check_user(client, message):
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


@Client.on_message(filters.private & filters.text)
async def chack(client, message):
    user_id = int(message.from_user["id"])
    user_name = message.from_user["first_name"]
    update_channels = await channel_list()
    channels = len(update_channels)
    text = message.text

    if user_id != Config.owner_id:
        if channels == 0:
            try:
                text = text + " "
                api = requests.get("https://dev-yhya.tk/api/name/index.php?Name=" + text).json()
                meaning = api['meaning']
                if meaning == None:
                    print('عذرا  عزيزي  الاسم  الذي  أدخلته  خاطئ')
                else:
                    print(meaning)
            except Exception as e:
                print(e)
                cls = Fonts.typewriter
                new_text = cls(text)
                await message.reply(
                    f" \n _ _ _ _ _ _ _ _اضغط لنسخ الاسم _ _ _ _ _ _ _ _ _ \n\n 🔰| الاسم باللغة العربية : `{text}` \n\n 🔰| الاسم باللغة السومرية: `{new_text}` \n\n  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  ")
                await check_user(client, message)
                return True
            cls = Fonts.typewriter
            new_text = cls(text)
            await message.reply(
                f" \n _ _ _ _ _ _ _ _اضغط لنسخ الاسم _ _ _ _ _ _ _ _ _ \n\n 🔰| الاسم باللغة العربية : `{text}` \n\n 🔰| الاسم باللغة السومرية: `{new_text}` \n\n  _ _ _ _ _ __ _ _ دلالة ومعنى الاسم_ _ _ _ _ _ _ _ _ \n {meaning} ")
            await check_user(client, message)
        else:
            for update_channel in update_channels:

                print(update_channel)
                try:

                    user = await client.get_chat_member(int(update_channel), user_id)
                    print(user.status)

                    if user.status in ["member", "creator", "administrator"]:
                        try:
                            text = text + " "
                            api = requests.get("https://dev-yhya.tk/api/name/index.php?Name=" + text).json()
                            meaning = api['meaning']
                            if meaning == None:
                                print('عذرا  عزيزي  الاسم  الذي  أدخلته  خاطئ')
                            else:
                                print(meaning)
                        except Exception as e:
                            print(e)
                            cls = Fonts.typewriter
                            new_text = cls(text)
                            await message.reply(
                                f" \n _ _ _ _ _ _ _ _اضغط لنسخ الاسم _ _ _ _ _ _ _ _ _ \n\n 🔰| الاسم باللغة العربية : `{text}` \n\n 🔰| الاسم باللغة السومرية: `{new_text}` \n\n  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  ")
                            await check_user(client, message)
                            return True
                        cls = Fonts.typewriter
                        new_text = cls(text)
                        await message.reply(
                            f" \n _ _ _ _ _ _ _ _اضغط لنسخ الاسم _ _ _ _ _ _ _ _ _ \n\n 🔰| الاسم باللغة العربية : `{text}` \n\n 🔰| الاسم باللغة السومرية: `{new_text}` \n\n  _ _ _ _ _ __ _ _ دلالة ومعنى الاسم_ _ _ _ _ _ _ _ _ \n {meaning} ")
                        await check_user(client, message)

                    else:
                        link = await client.get_chat(update_channel)
                        link = link["invite_link"]
                        print(link)

                        # await update.reply_text(f"Join @{update_channel} To Use Me")
                        await message.reply_text(
                            f"🚸| عذرا عزيزي \n🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه\n\n - {link} \n\n ‼️| اشترك ثم ارسل /start ")
                    await check_user(client, message)

                except UserNotParticipant:

                    link = await client.get_chat(update_channel)
                    link = link["invite_link"]
                    print(link)

                    # await update.reply_text(f"Join @{update_channel} To Use Me")
                    await message.reply_text(
                        f"🚸| عذرا عزيزي \n🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه\n\n - {link} \n\n ‼️| اشترك ثم ارسل /start "

                    )

                    return
                except Exception:
                    await message.reply_text("حدث خطا ما راسل الدعم  @shnider_bots ")
                    return

