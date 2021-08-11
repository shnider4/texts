#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Prince Mendiratta
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



import requests
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from .fonts import Fonts
from mongodb.channels import channel_list


from sample_config import Config





@Client.on_message( filters.private & filters.text )
async def chack(client, message):
    user_id = int(message.from_user["id"])
    user_name = message.from_user["first_name"]
    update_channels =await channel_list()
    channels = len(update_channels)
    text = message.text
    if user_id != Config.owner_id:
        if channels == 0 :
            if text == "/start":
                textq = "ارسل اسمك  لزغرفتة بالسومرية مثل \n `احمد : 𒅈𒍣` \n `زينب : 𒈨𒈠𒀭 ` "
                await message.reply(textq)
            else:
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
                    return True
                cls = Fonts.typewriter
                new_text = cls(text)
                await message.reply(
                    f" \n _ _ _ _ _ _ _ _اضغط لنسخ الاسم _ _ _ _ _ _ _ _ _ \n\n 🔰| الاسم باللغة العربية : `{text}` \n\n 🔰| الاسم باللغة السومرية: `{new_text}` \n\n  _ _ _ _ _ __ _ _ دلالة ومعنى الاسم_ _ _ _ _ _ _ _ _ \n {meaning} ")
        else:
            for update_channel in update_channels:

                print(update_channel)
                try:

                    user = await client.get_chat_member(int(update_channel), user_id)
                    print(user.status)

                    if user.status in ["member", "creator", "administrator"]:
                        if text == "/start":
                            textq = "ارسل اسمك  لزغرفتة بالسومرية مثل \n `احمد : 𒅈𒍣` \n `زينب : 𒈨𒈠𒀭 ` "
                            await message.reply(textq)
                        else:
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
                                return True
                            cls = Fonts.typewriter
                            new_text = cls(text)
                            await message.reply(
                                f" \n _ _ _ _ _ _ _ _اضغط لنسخ الاسم _ _ _ _ _ _ _ _ _ \n\n 🔰| الاسم باللغة العربية : `{text}` \n\n 🔰| الاسم باللغة السومرية: `{new_text}` \n\n  _ _ _ _ _ __ _ _ دلالة ومعنى الاسم_ _ _ _ _ _ _ _ _ \n {meaning} ")

                    else:
                        link = await client.get_chat(update_channel)
                        link = link["invite_link"]
                        print(link)

                        # await update.reply_text(f"Join @{update_channel} To Use Me")
                        await message.reply_text(
                            f"🚸| عذرا عزيزي \n🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه\n\n - {link} \n\n ‼️| اشترك ثم ارسل /start ")


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