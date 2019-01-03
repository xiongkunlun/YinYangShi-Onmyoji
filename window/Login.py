import os
from window.Core import *

loginPath = basePath + "login/"
loginTemp = loadTemps(loginPath)


def start():
    # os.system(
    #     "E:\\\"Program Files (x86)\"\Onmyoji\Launch.exe")
    # time.sleep(10)
    count = 1
    while count < 100:
        time.sleep(1)
        login()
        count = count + 1
        print(count)


def login():
    gps = AutoFilter(loginTemp)
    if gps:
        if gps[0]:
            click1(gps)


start()
