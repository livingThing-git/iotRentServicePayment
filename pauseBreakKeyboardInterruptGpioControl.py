import curses
import threading
import time
import RPi.GPIO as GPIO

key = 0
in1 = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)

def ligth():
    GPIO.output(in1, False)
    cond = True
    try:
        while cond:
            if key != ord('q'): 
                for x in range(5):
                    GPIO.output(in1, True)
                    time.sleep(0.1)
                    GPIO.output(in1, False)
                GPIO.output(in1, True)
                for x in range(4):
                    GPIO.output(in1, True)
                    time.sleep(0.05)
                GPIO.output(in1, True)
            else:
                GPIO.output(in1, False)
                cond = False
                break
    except KeyboardInterrupt:
        GPIO.cleanup()
    

def recieve_input():
    screen = curses.initscr()
    curses.cbreak
    screen.keypad(1)
    global key
    screen.addstr("Enter q to quit")
    screen.refresh
    cond = True
    
    while cond:
        try:
            if key != ord('q'):                
                y = threading.Thread(target=printKey)
                y.start()           
            
            key = screen.getch()
            screen.addch(key)
            screen.refresh()
        except KeyboardInterrupt:
            GPIO.cleanup()
            break
    curses.endwin

def printKey():
    cond = True
    while cond:
        if key != ord('q'):
            print("program start")
            ligth()
        else:
            print("press:"+ str(chr(key)))
            GPIO.output(in1, False)
            cond = False
            

if __name__=="__main__":
    x = threading.Thread(target=recieve_input)
    x.start()
    x.join
