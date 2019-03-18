# 限时组队，自动点击加入，如果没有加入就刷新
from window.Core import *
from window.Outdoor import fight

joinPath = basePath + "join/"
refreshPath = basePath + "refresh/"

joinTemp = loadTemps(joinPath)
refreshTemp = loadTemps(refreshPath)


def AutoJoin():
    cou = 1
    while cou < 1000:
        gps = AutoFilter(joinTemp)
        fgps = AutoFilter(refreshTemp)
        if gps:
            if gps[0]:
                # circleimg(gps)   #存储照片
                click1(gps)
        elif fgps:
            if fgps:
                if fgps[0]:
                    click1(fgps)
        cou = cou + 1
        # time.sleep(0.1)


if __name__ == '__main__':
    # joinTemp = loadTemps(joinPath)
    # refreshTemp = loadTemps(refreshPath)
    # #自己使用，可以注释掉下面的内容
    # # root = tkinter.Tk()
    # # result = tkinter.messagebox.askokcancel('提示',
    # #                                         '该工具仅为个人研究爱好，不得用于商业目的，谢绝修改，不得传播。产生后果与作者无关\n'
    # #                                         '使用方 法：第一步，修改痒痒鼠桌面版的分辨率为 640 1024，方法请百度\n'
    # #                                         '第二步，请确认已经选中了庭院-组队-某种队伍\n'
    # #                                         '第三步，打开脚本join.exe\n'
    # #                                         '按照0.5秒一次的频率去寻找《加入》按钮或者自动《刷新》当前组队页面，累计执行100次后自动停止\n'
    # #                                         '非组队界面无效\n'
    # #                                         '不适合：非庭院组队的所有其他都不适合!\n'
    # #                                         '怀疑有恶意软件的，请查看源码，移步https://github.com/xiongkunlun/yys\n'
    # #                                         '源码里面还有其他功能，都是基于图像识别做的小工具，觉得还行请在github点一个星\n'
    # #                                         '祝各位都有一头duangduangduang加特技的头发\n')
    # #if result:
    AutoJoin()

