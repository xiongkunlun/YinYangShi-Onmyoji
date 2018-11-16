from window.Util import *

storyPath = basePath + "story/"
homePath = basePath + "home/"


# 庭院场景
def home():
    # 保存一张截图
    get_array()
    print("进入庭院")
    if checkHome():
        if checkStory():
            while not checkHome():
                intoStory()
            print("当前剧情处理完成")
    else:
        print("当前场景不是庭院,准备野外扫图")
        while not checkHome():
            intoStory()
        print("当前剧情处理完成")


# 检查有没剧情
def checkStory():
    storyTemp = cv2.imread(homePath + "story.png", 0)
    if checkMatch(storyTemp):
        print("发现新剧情，进入剧情")
        img = cv2.imread(save_name, 0)
        res = cv2.matchTemplate(img, storyTemp,
                                cv2.TM_CCOEFF_NORMED)
        gps = []
        loc = np.where(res >= threshold)  # 匹配程度大于%80的坐标y,x
        for pt in zip(*loc[::-1]):  # *号表示可选参数
            gps.append(pt)
        click1(gps)
        time.sleep(1)
        return True
    return False


# 进入剧情,执行战斗，剧情结束后，会自动回到庭院，如果没有剧情，就会进入探索循环
def intoStory():
    print("当前场景为剧情中")
    temps = loadTemps(storyPath)
    gps = AutoFilter(temps)
    click1(gps)


# 检查当前是否为庭院
def checkHome():
    homeTemp = cv2.imread(homePath + "home.png", 0)
    homeTemp1 = cv2.imread(homePath + "home1.png", 0)
    if checkMatch((homeTemp, homeTemp1)):
        print("当前场景为庭院")
        return True
    else:
        print("当前场景不是庭院")
        return False


# 检查探索，进入探索
def out():
    temp = cv2.imread("out.png", 0)
    gps = AutoFilter([temp])
    click1(gps)


count = 1
while count < 1000:
    home()
    count = count + 1
