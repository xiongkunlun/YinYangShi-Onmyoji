import datetime

from window.Core import *

pkPath = basePath + "PK"

pkTemp = loadTemps(pkPath)
exitTmep = cv2.imread(pkPath + "/exit.png", 0)
fightTmep = cv2.imread(pkPath + "/fight.png", 0)
okTmep = cv2.imread(pkPath + "/ok.png", 0)
failTmep = loadTemps(pkPath + "/result")


def AutoExit():
    gps = AutoFilter([okTmep, okTmep])
    if gps:
        click1(gps)
        time.sleep(0.5)
    gps = AutoFilter([exitTmep, exitTmep])
    if gps:
        click1(gps)
        time.sleep(0.5)
    gps = AutoFilter([fightTmep, fightTmep])
    if gps:
        click1(gps)
        time.sleep(0.5)
    gps = AutoFilter(failTmep)
    if gps:
        click1(gps)
        time.sleep(0.5)


count = 0
while count < 5000:
    count = count + 1
    print(count)
    AutoExit()
