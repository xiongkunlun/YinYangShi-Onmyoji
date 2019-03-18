from window.Core import *

login_name = "登录"
loginPath = basePath + "login/"
loginTemp = loadTemps(loginPath)
homeExplorePath = basePath + 'homg_explore/'
homeExploreTemp = loadTemps(homeExplorePath)
accountFlag = True


def start():
    os.system(
        "E:\\\"Program Files (x86)\"\Onmyoji\Launch.exe")
    time.sleep(2)
    count = 1
    while count < 100 and accountFlag:
        app_hwnd = win32gui.FindWindow(None, app_name)
        print("app_hwnd",app_hwnd)
        time.sleep(1)
        login()
        count = count + 1
        print(count)
    print("complete login")


def login():
    global accountFlag
    loginHwnd = win32gui.FindWindow(None, login_name)
    if loginHwnd:
        print('in login frame:', loginHwnd)
        gps = AutoFilter(loginTemp, loginHwnd)
        if gps:
            if gps[0]:
                img = get_array(loginHwnd)
                circleimg(gps, img)
                click1(gps, loginHwnd)
                accountFlag = False


# global 无法修改core中的 app_hwnd 的句柄值，不知道为啥
def selectChannel():
    global app_hwnd
    app_hwnd = win32gui.FindWindow(None, app_name)
    channelFlag = True
    while channelFlag:
        gps = AutoFilter(loginTemp)
        checkAndClick(gps)

        gps = AutoFilter(homeExploreTemp)
        channelFlag = checkAndClick(gps)


def checkAndClick(gps):
    if gps:
        if gps[0]:
            click1(gps)
            time.sleep(1)
            return False


start()
selectChannel()
