import time
import random
import datetime


 #generate times 
def generate_times():
    times = []
    for i in range(10):
        hour= random.randint(0,23)
        minute = random.randint(0,59)
        times.append((hour,minute))
        
    return sorted(times)

#sleep
def wait_until(hour,minute):
    while True:
        now = datetime.datetime.now()
        if now.hour==hour and now.minute==minute:
            return
        time.sleep()
        
def loop():
    while True:
        schedule = generate_times
        now = datetime.datetime.now()
        for h,m in schedule:
            wait_until(h,m)
            print(f"Running task at {h}:{m}")
        time.sleep(60) #wait a minute before generating new schedule
        
if __name__ == "__main__":
    loop()
