from time import sleep
from pyrogram import Client
import logging


# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)





# Hesap
API_ID = "17253611"
API_HASH = "ec38639d1331e305f469bf0496c2a039"
TOKEN = "5575724170:AAHWj9-xYUnKzMBTxTHGRvcktpPyq1yIdhw" 
USERNAME = "5249642922"




# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID, "17253611"
    API_HASH, "ec38639d1331e305f469bf0496c2a039"
    bot_token=TOKEN,"5575724170:AAHWj9-xYUnKzMBTxTHGRvcktpPyq1yIdhw"
    plugins=dict(root="karabakhsozbot/plugins/"),
    workers=16
    )


# Oyun Verileri
oyun = {oyun}


# rating
rating = {skor}





# !!!!!!!!!!!!!! DEĞİŞTİR KESİNLİKLE !!!!!!!!!!!!!!!!
#      SAHİBİN USER ID'Sİ
OWNER_ID = 5249642922

