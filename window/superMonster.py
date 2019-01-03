# 检查超鬼王提示，有则点击，自动点击退治，自动准备开打

from window.Core import *

superPath = basePath + "superMonster/"
superTemp = loadTemps(superPath)


def findsuperMon():
    while True:
        time.sleep(2)
        gps = AutoFilter(superTemp)
        if gps:
            if gps[0]:
                print("发现超鬼王，开打")
                click1(gps)


        else:
            print("没有发现超鬼王")

findsuperMon()