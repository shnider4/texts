# By @TroJanzHEX
from pyrogram import Client
import os

from sample_config import Config


if True:
    plugins = dict(root="plugins")

    app = Client(
        "TroJanz",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300,
    )
    app.run()







