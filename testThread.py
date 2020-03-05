
    
import threading
import time

x = input()

def test_thread():

    x = input("Press enter when you hear the sound.")

def test_func():

    while thread.is_alive() and x=="x":
        while True:
            time.sleep(1)
            print("hello world")

    print("Thread is over. User heard a sound.")

thread = threading.Thread(target=test_thread)
thread.daemon = True
thread.start()
test_func()