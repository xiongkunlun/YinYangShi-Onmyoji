from window.Util import *
import threading

finishPath = basePath + "finish/"


def mythread():
    while True:
        print("1")
        finish_temps = loadTemps(finishPath)
        if checkMatch(finish_temps):
            print("奖励结算，休息3秒")
            gps1 = AutoFilter(finish_temps)
            click1(gps1)
            click1(gps1)
            time.sleep(2)
            gs = [(750, 500), (750, 600)]
            click1(gs)
            print("结算完成，点击屏幕")


t = threading.Thread(target=mythread, name="checkingFinish")
t.start()
t.join()
