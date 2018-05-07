'''
Title: Python clock because why the hell not
Author: Riley Carpenter
'''
import time
import sys
import os
if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"
while True:
    Currenttime = time.ctime()
    Hours1 = (Currenttime[11:13])
    Minutes1 = (Currenttime[14:16])
    Seconds = (Currenttime[17:19])
    print("The current time is",Hours1 + ":" + Minutes1 + ":" + Seconds)
    time.sleep(1)
    os.system(clearorcls)
