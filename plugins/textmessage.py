import requests

from pyrogram import Client, filters
from mongodb.channels import channel_list
from mongodb.members import members_list, add_members_to_db
from mongodb.users import add_client_to_db
from plugins.commands import owner_help
from plugins.fonts import Fonts
from sample_config import Config


@Client.on_message(filters.private & filters.text)
async def text (client, message):
    userid=str( message.from_user.id)
    owner_id =str( Config.owner_id)
    update_channel = await  channel_list()
    chats = await members_list()
    text = message.text
    print(chats)
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


    if userid in chats :
        try:
            text = text + " "
            api = requests.get("https://dev-yhya.tk/api/name/index.php?Name=" + text).json()
            meaning = api['meaning']
            if meaning == None:
                print('عذرا  عزيزي  الاسم  الذي  أدخلته  خاطئ')
        except Exception:
            cls = Fonts.typewriter
            new_text = cls(text)
            await message.reply(
                f" \n _ _ _ _ _ _ _ _اضغط لنسخ الاسم _ _ _ _ _ _ _ _ _ \n\n 🔰| الاسم باللغة العربية : `{text}` \n\n 🔰| الاسم باللغة السومرية: `{new_text}` \n\n  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  ")

            return True
        cls = Fonts.typewriter
        new_text = cls(text)
        await message.reply(
            f" \n _ _ _ _ _ _ _ _اضغط لنسخ الاسم _ _ _ _ _ _ _ _ _ \n\n 🔰| الاسم باللغة العربية : `{text}` \n\n 🔰| الاسم باللغة السومرية: `{new_text}` \n\n  _ _ _ _ _ __ _ _ دلالة ومعنى الاسم_ _ _ _ _ _ _ _ _ \n {meaning} ")

        print("ok elssss")


    else:
        for update_channel in update_channel:

            link = f"https://t.me/{update_channel}"

            print("no")
            await message.reply_text(
                        f"🚸| عذرا عزيزي \n🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه\n\n - {link} \n\n ‼️| اشترك ثم ارسل /start ",
                        disable_web_page_preview=True)
            await add_members_to_db(userid)


