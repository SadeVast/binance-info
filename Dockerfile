FROM python: latest

COPY main.py binanceinfo.py Telegramsender.py .gitignore

CMD ["python", "binanceinfo.py", "Telegramsender.py", ".gitignore",]