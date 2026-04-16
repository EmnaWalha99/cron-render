import time
import random
import datetime

# generate times
def generate_times():
    times = []
    for _ in range(100):
        hour = random.randint(18, 20)
        minute = random.randint(0, 59)
        times.append((hour, minute))

    return sorted(times)


# sleep until target time
def wait_until(hour, minute):
    target = datetime.datetime.now().replace(
        hour=hour,
        minute=minute,
        second=0,
        microsecond=0
    )

    # if time already passed today → skip
    if datetime.datetime.now() > target:
        return

    while True:
        now = datetime.datetime.now()

        if now >= target:
            return

        time.sleep(5)


def loop():
    while True:
        schedule = generate_times()

        print("New schedule:", schedule)

        for h, m in schedule:
            wait_until(h, m)
            print(f"Running task at {h:02d}:{m:02d}")

        time.sleep(60)  # wait before regenerating


if __name__ == "__main__":
    loop()