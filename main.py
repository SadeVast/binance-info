import time

import Telegramsender
import binanceinfo

for i in binanceinfo.get_binfo():
    print(i)
    Telegramsender.send_news_to_telegram(i)
    time.sleep(2)
