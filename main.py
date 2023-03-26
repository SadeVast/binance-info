import time
import Telegramsender
import binanceinfo
import info_db


def insert_binance_to_db():
    for a in binanceinfo.get_binfo():
        info_db.insert_into(info_db.create_connection(info_db.DATABASE),a)

if __name__ == '__main__':
    info_db.create_connection(info_db.DATABASE)
    info_db.create_table(info_db.create_connection(info_db.DATABASE))
    insert_binance_to_db()

    for a in info_db.get_all_news(info_db.create_connection(info_db.DATABASE)):
        Telegramsender.send_news_to_telegram(a)
        time.sleep(2)

