from window.Util import *

juexingPath = basePath + "juexing/"
teaminvitePath = basePath + "teaminvite/"
eatPath = basePath + "eat/"


def fight():
    finish_temps = loadTemps(eatPath)
    if checkMatch(finish_temps):
        print("有吃的啦，休息1秒")
        gps1 = AutoFilter(finish_temps)
        click1(gps1)
        time.sleep(3)
        click1(gps1)
        time.sleep(0.5)
        gs = [(284, 144), (284, 144)]
        click1(gs)
