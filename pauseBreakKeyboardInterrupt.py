import curses
import threading

key = 0

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
            break
    curses.endwin

def printKey():
    cond = True
    while cond:
        if key != ord('q'):
            print("program start")
        else:
            print("press:"+ str(chr(key)))
            cond = False
            

if __name__=="__main__":
    x = threading.Thread(target=recieve_input)
    x.start()
    x.join
