import os

class Config(object):
    LOGGER = False
    TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN', None) 
    TG_DUMP_CHANNEL = int(os.environ.get("TG_DUMP_CHANNEL", "0"))
    URL = os.environ.get('URL', "")
    PORT = int(os.environ.get('PORT', 8080)) 
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", "")
    
class Development(Config):
    LOGGER = True
