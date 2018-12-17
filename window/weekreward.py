import datetime

from window.Core import *

weekpath = basePath + "/weekreward"
weekTemp = loadTemps(weekpath)


def AutoExit():
    gps = AutoFilter(weekTemp)
    if gps:
        click1(gps)
        print(gps)
        time.sleep(2)
        click1(gps)


count = 0
while count < 50000:
    count = count + 1
    print(count)
    AutoExit()
