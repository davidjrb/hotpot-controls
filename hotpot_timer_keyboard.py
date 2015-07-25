import time
import datetime
while True:
    run = raw_input("press enter to start")
    Elapsed = 0
    TimerSet = 5
    if run == "":
        datenow = time.strftime('%H:%M:%S')
        print "running"
        print "run signal recieved at", datenow, "duration:", TimerSet, "minutes"
        time.sleep(TimerSet)
        print "done"
