# 野外自动选26章，自动战斗
import datetime

from window.Core import *

bossPath = basePath + "/boss"
bossTemps = loadTemps(bossPath)

finishPath = basePath + "finish/"
chapterPath = basePath + "chapter/"
chapterNum = 4
fightPath = basePath + "fight/"
fightTem = loadTemps(fightPath)
fightallPath = basePath + "fightall/"
fightallTemp = loadTemps(fightallPath)
outdoorPath = basePath + "outdoor/"
type = 3
checkmovePath = basePath + "checkmove/"
direction = 0

checkMonsterPath = basePath + "checkmonster"
checkMonsterTeamPath = basePath + "checkMonsterTeam"

checkSecreatePath = basePath + "checksecreate"
checkTicketPath = basePath + "checkticket"
buyTicketPath = basePath + "buyticket"
expPath = basePath + "exp"
monPath = basePath + "mon"
coinPath = basePath + "coin"
home_explorePath = basePath + "home_explore"

lastTime = 0
# 神秘商店出现的最长时间，单位为分钟
appearTime = 30

homeTemp = cv2.imread(outdoorPath + "outdoor.png", 0)
homeTemp1 = cv2.imread(outdoorPath + "people.png", 0)
secreteTemps = loadTemps(checkSecreatePath)
ticketTemp = loadTemps(checkTicketPath)

expTemp = loadTemps(expPath)
coinTemp = loadTemps(coinPath)
monsterTemp = loadTemps(monPath)
total = 0
# 功能性点击按钮，除了打怪
functionTemps = loadTemps(fightPath)

# 1=经验怪，2=金币怪，3=红达摩
fightType = 1


def outdoor():
    count = 1
    if count < 100000:
        if type == 3:
            while True:
                if checkOut():
                    time.sleep(1)
                    if checkMonster():
                        # 点击右侧妖气头像
                        temps = loadTemps(checkMonsterPath)
                        gps = AutoFilter(temps)
                        click1(gps)
                        time.sleep(1.5)
                        # 创建组队
                        gps = AutoFilter(temps)
                        click1(gps)
                        time.sleep(1.5)
                        # 点击确定队形
                        tempteam = loadTemps(
                            checkMonsterTeamPath)
                        gps = AutoFilter(tempteam)
                        click1(gps)
                        time.sleep(1.5)
                        # 队员到位，开始战斗
                        tempteam = loadTemps(
                            checkMonsterTeamPath)
                        gps = AutoFilter(tempteam)
                        click1(gps)
                        time.sleep(1.5)
                        # 队员到位，开始战斗
                        tempteam = loadTemps(
                            checkMonsterTeamPath)
                        gps = AutoFilter(tempteam)
                        click1(gps)
                        time.sleep(1)
                    print("选章")
                    intoChapter()
                    time.sleep(random.uniform(0.2, 0.5))
                    fight()
                    count = count + 1
                else:
                    fight()
                    count = count + 1


def checkSecreateStore():
    global lastTime
    # 检查神秘商店

    if checkMatch(secreteTemps):
        # 如果上次时间距离现在不足，则不点击商店
        nowTime = datetime.datetime.now()
        if int(nowTime) - int(lastTime) > appearTime * 60:
            lastTime = nowTime
            gps = AutoFilter(secreteTemps)
            click1(gps)
            time.sleep(0.5)
            # 检查有无蓝票 -排除掉勾玉不足
            if checkMatch(ticketTemp):
                ticketgps = AutoFilter(ticketTemp)
                click1(ticketgps)
                time.sleep(0.5)
                # 检查购买按钮
                buytemp = loadTemps(buyTicketPath)
                # 检查有无蓝票 -排除掉勾玉不足
                if checkMatch(buytemp):
                    buygps = AutoFilter(buytemp)
                    click1(buygps)
                    time.sleep(0.5)


# 根据选择的章节temp，找到图标，点击探索，进入场景
def intoChapter():
    global total
    global direction
    total = 0
    direction = 0
    # 这里有问题，不能获取到章节图标的定位。暂时采取固定坐标的方式
    ps1 = (global_left + 870, global_top + 510)
    ps2 = (707, 480)
    gps1 = (ps1, ps2)
    # temp = selectChapter()
    # gps = AutoFilter(temp)
    # print(gps)
    click1(gps1)
    time.sleep(random.uniform(0.4, 0.8))
    # exploreTemp = cv2.imread(chapterPath + "explore.png", 0)
    # gps = AutoFilter(exploreTemp)
    gps = (ps2, ps1)
    click1(gps)


def fight():
    global total
    global direction
    # 检查boss
    bossgps = AutoFilter(bossTemps)
    if bossgps:
        click1(bossgps)
        time.sleep(1)
        click1(bossgps)
    expgps = 0
    if fightType == 1:
        expgps = AutoFilter(expTemp)
    elif fightType == 2:
        expgps = AutoFilter(coinTemp)
    elif fightType == 3:
        expgps = AutoFilter(fightallTemp)
    mongps = AutoFilter(monsterTemp)
    point = get_nearest_point(expgps, mongps)
    if point:
        print("点击")
        print(point)
        click1([point])
    gps = AutoFilter(functionTemps)
    click1(gps)
    time.sleep(0.5)
    finish_temps = loadTemps(finishPath)
    if checkMatch(finish_temps):
        print("奖励结算，休息3秒")
        gps1 = AutoFilter(finish_temps)
        click1(gps1)
        time.sleep(1.5)
        click1(gps1)
        total = 0
        return
    move_temps = loadTemps(checkmovePath)
    if checkMatch(move_temps):
        if 0 <= direction < 11:
            gs = [(820, 530), (780, 600)]
            click1(gs)
            direction = direction + 1
            total = total + 1
            print("向右移动第%s次" % str(direction))
        elif direction == 11:
            direction = -10
        else:
            direction = direction + 1
            gs = [(280, 530), (600, 550)]
            click1(gs)
            print("向左移动第%s次" % str(direction + 11))
            total = total + 1
    time.sleep(0.5)
    if total > 15:
        ex1 = (40, 80)
        ex2 = (40, 85)
        gps1 = (ex1, ex2)
        click1(gps1)
        total = 0
        direction = 0


# 选择章节，返回章节的temp
def selectChapter():
    if chapterNum:
        temp = cv2.imread(
            chapterPath + str(chapterNum) + ".png",
            0)
        return temp


# 检查是否在野外
def checkOut():
    if checkMatch((homeTemp, homeTemp1)):
        global direction
        direction = 0
        print("清除移动次数")
        # print("当前场景为野外")
        return True
    else:
        # print("当前场景不是野外")
        return False


# 检查有没有石距，挂机不要打石距，御魂低也不要打石距
def checkShip():
    pass


# 检查有没有妖气封印-卖药郎
def checkMonster():
    medicalTemps = loadTemps(checkMonsterPath)
    if checkMatch(medicalTemps):
        # print("当前场景为野外")
        return True
    else:
        # print("当前场景不是野外")
        return False


# 进入家后，自动点击
def goOutDoor():
    exploreTemp = loadTemps(home_explorePath)
    if checkMatch(exploreTemp):
        gps = AutoFilter(exploreTemp)
        # circleimg(gps)
        click1(gps)
        time.sleep(2)
        return True
    else:
        return False;


if __name__ == '__main__':
    outdoor()
