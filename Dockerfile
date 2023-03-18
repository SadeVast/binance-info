FROM python: latest

COPY ./binance-info

CMD ["python" "./main.py"]