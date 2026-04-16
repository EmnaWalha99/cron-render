import datetime
import requests

def notify(message):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": "az5be9kwk7qnar2832w4hhvmktrphx",
            "user": "u6pwcttr7knnzzuf7rxp6xa81wae4j",
            "message": "hello world"
        }
    )

def run_task():
    print(f"Task is running at {datetime.datetime.now()}")