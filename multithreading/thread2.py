import threading
import time


def display():
    for i in range(1, 10):
        time.sleep(5)
        print("child thread executing")
    print(threading.currentThread().getName())


display()
for i in range(1, 10):
    time.sleep(5)
    print("main thread executing")
print(threading.currentThread().getName())
