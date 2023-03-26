FROM python:latest

COPY ("main.py","binanceinfo.py","Telegramsender.py","info_db.py")
COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python","./main.py"]