import logging
import requests
import os
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())
# Use when test on localhost
# TELEGRAM_API = (os.getenv('TGSTOKEN'))
# API_URL = f"https://api.telegram.org/bot{TELEGRAM_API}/sendMessage"
# CHAT_ID = (os.getenv('TGSID'))
# Use when build in image
TGSTOKEN=os.environ["TGSTOKEN"]
TGSID=os.environ["TGSID"]
def send_news_to_telegram(message):
    """
    Send messages from db to telegram
    :param message:
    :return:
    """

    try:
        response = requests.post(
            API_URL,
            json={
                "chat_id": CHAT_ID,
                "text": f"{message[0]} {message[1]}"
            },
        )
        if response.status_code == 200:
            logging.info(
                f"Sent: {response.reason}. Status code: {response.status_code}"
            )
        else:
            logging.error(
                f"Not sent: {response.reason}. Status code: {response.status_code}"
            )
    except Exception as err:
        logging.error(err)


