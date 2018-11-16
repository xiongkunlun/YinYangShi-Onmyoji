import win32con
import win32gui
import win32api
from PIL import ImageGrab
import time
import random
import cv2
import numpy as np
import os
import math

# 2068550500 国际服，一只彼岸花

# 桌面版的标题为“阴阳师-网易游戏”,腾讯手游助手【极速傲引擎】
app_name = "阴阳师-网易游戏"
save_name = "D://HAHA.png"
basePath = "C:\\Users\\Administrator\\PycharmProjects\\yys\\window\\"
threshold = 0.9  # 匹配度
# 是否是第一次前置窗口
isHead = True

# 传入截图保存位置和命名，比如"D://HAHA.PNG",存储截图，并返回窗口矩形左上右下四个边距。
def get_array():
    global isHead
    # 根据窗口名字，查找到窗口，返回句柄
    hwnd = win32gui.FindWindow(None, app_name)
    if not hwnd:
        print('window not found!')
        exit(0)
    else:
        if isHead:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            # 强行显示界面
            win32gui.SetForegroundWindow(hwnd)  # 将窗口提到最前
            isHead = False
        # # 截屏
        game_rect = win32gui.GetWindowRect(hwnd)  # 获取句柄所在矩形
        # print('当前句柄为:%s,窗口名为:%s' % (hwnd, app_name))
        # print(game_rect)
        src_image = ImageGrab.grab(game_rect)  # 根据矩形位置，截取图片
        img = src_image.convert('L')
        image = np.asarray(img)  # 从截图获得np
        return image


# 加载文件夹下所有图标，返回temps集合
def loadTemps(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.png':
                temp = cv2.imread(os.path.join(root, file),
                                  0)
                L.append(temp)
    return L


# 传入文件地址和temps，传回可以点击的点集合
def AutoFilter(temps):
    img = get_array()
    gps = []
    for temp in temps:
        res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)  # 匹配程度大于%80的坐标y,x
        for pt in zip(*loc[::-1]):  # *号表示可选参数
            gps.append(pt)
            if gps:
                return gps


def checkMatch(temps):
    gps = AutoFilter(temps)
    if gps:
        if gps[0]:
            return True
        else:
            return False
    else:
        return False

# 传入鼠标定位和矩形边距，左键单击
def click1(gps):
    if gps:
        if gps[0]:
            x = random.randint(10, 20) + gps[0][0]
            y = random.randint(5, 10) + gps[0][1]
            win32api.SetCursorPos((x, y))
            # time.sleep(0.1)
            # 下面的参数分别为：（事件类型，x坐标，y坐标，滚轮滑动数量，附加32位值）
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(random.uniform(0.2, 0.4))
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


# 指定大小截图，此处不使用
def cutPic(src_image):
    width, hight = src_image.size  # 获取图片宽高
    left_box = (0, 0, width / 3 * 2,
                hight / 3 * 2)  # 创建截图区域，注意这里的前两个参数是目标窗口的左上角。
    image_left = src_image.crop(
        left_box)  # 从母版的左上角开始，进行截图，不是整个显示器
    image_left.show()
    image_left.save("D://HALF.png")


def callen(egps, fgps):
    x = egps[0] - fgps[0]
    y = egps[1] - fgps[1]
    return math.sqrt(abs(x) * abs(x) + abs(y) * abs(y))


def get_nearest_point(expgps, fightgps):
    distance = 1000
    point = (0, 0)
    if expgps and fightgps:
        for e in expgps:
            for f in fightgps:
                if distance > callen(e, f):
                    distance = callen(e, f)
                    point = f
        return point
    else:
        return
def infoimg(img):
    print(type(img))
    print(img.shape)