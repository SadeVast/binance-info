import time
from binance.client import Client
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

API_KEY = (os.getenv('API_KEY'))
API_SECRET = (os.getenv('API_SECRET'))

client = Client(API_KEY, API_SECRET)


# print(client.get_account())
def get_binfo():
    info = client.get_exchange_info()
    print(info.keys())
    print(info.values())
    symbols = info["symbols"]
    print(symbols)

    for sym in symbols:
        print(sym)
        print("====================================")
        time.sleep(2)
        yield sym



# for k, v in info.items():
#     print(f"Key: {k} - Value: {v}")
#     time.sleep(5)
#     print("====================================")
# print(client.get_account())
