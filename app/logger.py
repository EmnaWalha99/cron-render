import datetime

def log(msg):
    filename = f"logs/log_{datetime.date.today()}.txt"
    with open(filename, "a") as f:
        f.write(msg + "\n")