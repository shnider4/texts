# By @TroJanzHEX


import os

class Config(object):
    
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    APP_ID = int(os.environ.get("API_ID", 12345))
    
    API_HASH = os.environ.get("API_HASH", "")
    MONGO_URL =  os.environ.get("MONGO_URL",  "")
    owner_id =int(1827146773)



    
