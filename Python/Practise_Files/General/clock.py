import time


try:
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time, end = "\r")
        time.sleep(1)

except KeyboardInterrupt:
    print("Thank you!")