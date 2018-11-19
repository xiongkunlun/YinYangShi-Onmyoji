#尝试后台根据句柄截图
# 对后台应用程序截图，程序窗口可以被覆盖，但如果最小化后只能截取到标题栏、菜单栏等。
import win32gui
import win32ui
import win32con
from ctypes import windll
from PIL import Image
import numpy as np
import cv2
import win32gui
import win32api
import win32con

app_name = "阴阳师-网易游戏"

# 获取要截取窗口的句柄
hwnd = win32gui.FindWindow(None, app_name)

# 获取句柄窗口的大小信息
# 可以通过修改该位置实现自定义大小截图
left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

# 返回句柄窗口的设备环境、覆盖整个窗口，包括非客户区，标题栏，菜单，边框
hwndDC = win32gui.GetWindowDC(hwnd)

# 创建设备描述表
mfcDC  = win32ui.CreateDCFromHandle(hwndDC)

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
mem_dc.BitBlt((0, 0), (w, h), img_dc, (100, 100), win32con.SRCCOPY)

# 改变下行决定是否截图整个窗口，可以自己测试下
# result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
print(result)

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

# # 存储截图
# if result == 1:
#     #PrintWindow Succeeded
#     im.save("D://1/test.png")
#     # im.show()

# 内存释放
win32gui.DeleteObject(saveBitMap.GetHandle())
saveDC.DeleteDC()
mfcDC.DeleteDC()
win32gui.ReleaseDC(hwnd, hwndDC)

p1 = (870, 510)
tmp = win32api.MAKELONG(p1[0], p1[1])
win32api.SendMessage(hwnd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, tmp)
win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

# # PIL简单实现截图，只能截图最上层窗口
# from PIL import Image,ImageGrab
# bbox = (1085, 102, 1368, 373)
# img = ImageGrab.grab(bbox)
# # img = ImageGrab.grab()
# img.save("pixel.png")
# img.show()
#
# # 图像存储：应用cv2
# signedIntsArray = saveBitMap.GetBitmapBits(True)
# img = np.fromstring(signedIntsArray, dtype='uint8')
# img.shape = (height,width,4)
# cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
#
# 图像存储应用numpy

