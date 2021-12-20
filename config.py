import os

class Config(object):
    LOGGER = False
    TG_BOT_TOKEN = "5084464597:AAGUzrQGFDHa7WWHBlGTr2D8jO5MZsqWTQM"
    TG_DUMP_CHANNEL = "-1001518142903"
    URL = os.environ.get('URL', "")
    APP_ID = "2698821"
    API_HASH = "4af625c75eb9e72e1b228411b0c7cd42"
    
class Development(Config):
    LOGGER = True
