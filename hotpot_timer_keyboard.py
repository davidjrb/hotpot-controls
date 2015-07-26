import time
from termios import tcflush, TCIFLUSH
import time,sys

while True:

    run = raw_input("press enter to start")
    TimerSet = 5
    if run == "":
        datenow = time.strftime('%H:%M:%S')
        print datenow, "running"
        time.sleep(TimerSet)
        tcflush(sys.stdin, TCIFLUSH)
        datenow = time.strftime('%H:%M:%S')
        print datenow, "done"
