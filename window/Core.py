import time
import random
import os
import math
import win32ui
from ctypes import windll
from PIL import Image
import numpy as np
import cv2
import win32gui
import win32api
import win32con

# 2068550500 国际服，一只彼岸花


img = ""
# 桌面版的标题为“阴阳师-网易游戏”,腾讯手游助手【极速傲引擎】
app_name = "阴阳师-网易游戏"
save_name = "D://HAHA.png"
basePath = "C:\\Users\\Administrator\\PycharmProjects\\yys\\window\\"
threshold = 0.95  # 匹配度
# 是否是第一次前置窗口
isHead = True
hwnd = win32gui.FindWindow(None, app_name)
global_left = 0
global_top = 0
global_size = [0, 0]


# 传入截图保存位置和命名，比如"D://HAHA.PNG",存储截图，并返回窗口矩形左上右下四个边距。
def get_array():
    global isHead,global_top,global_left,global_size
    # 根据窗口名字，查找到窗口，返回句柄
    if not hwnd:
        print('window not found!')
        exit(0)
    elif isHead:
        # 这个地方有问题，准备做一个最小化就自动还原
        # if win32gui.IsIconic(hwnd):
        #     #     win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        #     win32gui.ShowWindow(hwnd, 0)
        #     time.sleep(0.5)
        if isHead:
            # win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            # # 强行显示界面
            # win32gui.SetForegroundWindow(hwnd)  # 将窗口提到最前
            # isHead = False
            # # 截屏
            left, top, right, bot = win32gui.GetWindowRect(
                hwnd)
            global_left = left
            global_top = top
            global_size = (left, top)
            w = right - left
            h = bot - top

            # 返回句柄窗口的设备环境、覆盖整个窗口，包括非客户区，标题栏，菜单，边框
            hwndDC = win32gui.GetWindowDC(hwnd)

            # 创建设备描述表
            mfcDC = win32ui.CreateDCFromHandle(hwndDC)

            # 创建内存设备描述表--compatible兼容的设备描述表
            saveDC = mfcDC.CreateCompatibleDC()

            # 创建位图对象准备保存图片
            saveBitMap = win32ui.CreateBitmap()
            # 为bitmap开辟空间
            saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
            saveDC.SelectObject(saveBitMap)

            # 截图至内存设备描述表
            img_dc = mfcDC
            mem_dc = saveDC
            mem_dc.BitBlt((0, 0), (w, h), img_dc,
                          (100, 100),
                          win32con.SRCCOPY)

            # 改变下行决定是否截图整个窗口，可以自己测试下
            # result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
            result = windll.user32.PrintWindow(hwnd,
                                               saveDC.GetSafeHdc(),
                                               0)
            # 获取位图信息
            bmpinfo = saveBitMap.GetInfo()
            bmpstr = saveBitMap.GetBitmapBits(True)
            # 生成图像
            im = Image.frombuffer(
                'RGB',
                (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
                bmpstr, 'raw', 'BGRX', 0, 1)
            src_img = im.convert('L')
            image = np.asarray(src_img)
            # cv2.imshow("", image)
            # cv2.waitKey(0)
            # # 存储截图
            # if result == 1:
            #     im.save("D://1/test.png")
            # 内存释放
            win32gui.DeleteObject(saveBitMap.GetHandle())
            saveDC.DeleteDC()
            mfcDC.DeleteDC()
            win32gui.ReleaseDC(hwnd, hwndDC)
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
    global img
    img = get_array()
    gps = []
    for temp in temps:
        res = cv2.matchTemplate(img, temp,
                                cv2.TM_CCOEFF_NORMED)
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
            x = gps[0][0]
            y = gps[0][1]
            point = (x, y)
            tmp = win32api.MAKELONG(point[0],
                                    point[1])
            print(global_left + point[0])
            print(global_top + point[1])
            win32api.SendMessage(hwnd,
                                 win32con.WM_MOUSEMOVE,
                                 win32con.MK_LBUTTON, tmp)
            win32api.SendMessage(hwnd,
                                 win32con.WM_LBUTTONDOWN,
                                 win32con.MK_LBUTTON, tmp)
            win32api.SendMessage(hwnd,
                                 win32con.WM_LBUTTONUP,
                                 win32con.MK_LBUTTON, tmp)


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
    dis = math.sqrt(abs(x) * abs(x) + abs(y) * abs(y))
    return dis


def get_nearest_point(expgps, fightgps):
    distance = 1000
    point = (0, 0)

    if expgps:
        print("识别到经验图标")
        if fightgps:
            print("识别到战斗图标")
            # circ  leimg(expgps, fightgps)
            for e in expgps:
                for f in fightgps:
                    if distance > callen(e, f):
                        distance = callen(e, f)
                        point = f
            return point
        else:
            return
    else:
        return


def infoimg(img):
    print(type(img))
    print(img.shape)


def circleimg(expgps, fgps):
    for e in expgps:
        cv2.circle(img, e, 20, (255, 0, 0), 0)
    for f in fgps:
        cv2.circle(img, f, 20, (255, 0, 0), 0)
    cv2.imwrite("D://HAHA1.png", img)
    print('存储照片')


#传入一个gps，进行标点存储
def circleimg(points):
    for p in points:
        cv2.circle(img, p, 20, (255, 0, 0), 0)
    cv2.imwrite("D://HAHA1.png", img)
    print('存储照片')
