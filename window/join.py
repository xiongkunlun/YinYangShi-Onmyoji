# 限时组队，自动点击加入，如果没有加入就刷新
from window.Core import *
from window.Outdoor import fight

joinPath = basePath + "join/"
refreshPath = basePath + "refresh/"

joinTemp = loadTemps(joinPath)
refreshTemp = loadTemps(refreshPath)


def AutoJoin():
    cou = 1
    while cou < 5000:
        gps = AutoFilter(joinTemp)
        fgps = AutoFilter(refreshTemp)
        if gps:
            if gps[0]:
                circleimg(gps)
                click1(gps)
        elif fgps:
            if fgps:
                if fgps[0]:
                    click1(fgps)
        else:
            fight()
        cou = cou + 1


AutoJoin()
