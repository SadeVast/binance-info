import time
import Telegramsender
import binanceinfo
import info_db


def insert_binance_to_db():
    for a in binanceinfo.get_binfo():
        info_db.insert_into(info_db.create_connection(info_db.DATABASE))


for i in binanceinfo.get_binfo():
    print(i)
    Telegramsender.send_news_to_telegram(i)
    time.sleep(2)
