#!/usr/local/bin/python3.6
from time import localtime,strftime,mktime
start_time = localtime()
print(f" Timer  started at {strftime('%X',start_time)}")
# Wait for user to stop timer
input("Press enter key to stop timer")
stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)
print(f" Timer  started at {strftime('%X',stop_time)}")
print(f" Total time: {difference}")
