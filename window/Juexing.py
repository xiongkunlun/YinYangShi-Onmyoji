# 觉醒暂时只能手动选择某一个副本，进入到组队界面，然后循环开始，循环邀请
from window.Core import *

juexingPath = basePath + "juexing/"
teaminvitePath = basePath + "teaminvite/"
teamfightPath = basePath + "teamfight/"


def team():
    count = 0
    while count < 1000000:
        checkMenber()
        # teamJuexing()
        # checkMenber()
        # time.sleep(random.uniform(0.3, 0.7))
        count = count + 1
        print(count)
    exit()


# 组队界面里，自动开始，结束后自动邀请
def teamJuexing():
    print("当前场景：组队模式")
    temps = loadTemps(juexingPath)
    gps = AutoFilter(temps)
    click1(gps)


def checkMenber():
    temp2 = loadTemps(teamfightPath)
    fightgps2 = AutoFilter(temp2)
    temp = loadTemps(teaminvitePath)
    invitegps = AutoFilter(temp)
    if fightgps2:
        if len(fightgps2) > 0:
            if 500 < invitegps[0][0] < 701 and 0 < \
                    invitegps[0][1] < 521:
                print("1")
                pass
            else:
                time.sleep(0.3)
                click1(fightgps2)
                time.sleep(random.uniform(0.3, 0.5))
                teamJuexing()
    else:
        teamJuexing()


team()
