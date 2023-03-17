FROM python: latest

COPY main.py binanceinfo.py Telegramsender.py

CMD ["python", "./binanceinfo"]