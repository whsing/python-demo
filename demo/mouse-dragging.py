#mouseDragging
# -*- coding: utf-8 -*-
import pyautogui
import time
import random

#各按钮位置
startPoint = (1295, 700)    #开始位置 位置
endPoint = (1281, 220)    #结束位置 位置
flotPX = 30 # 鼠标位置浮动的坐标差
dragMS = 500 # 拖动的时长，毫秒
floatDragMS = 100 # 拖动时长的浮动值，毫秒
sleepSec = 2 # 间隔时间，秒
floatSleepSec = 1 # 间隔时间，秒


def main():
    i = 0
    while True:
        startPointTemp = (randUpDown(startPoint[0], flotPX), randUpDown(startPoint[1], flotPX))    #开始位置 随机浮动
        endPointTemp = (randUpDown(endPoint[0], flotPX), randUpDown(endPoint[1], flotPX))    #结束位置 随机浮动
        #print(startPointTemp)
        #print(endPointTemp)
        pyautogui.moveTo(startPointTemp[0], startPointTemp[1])
        pyautogui.dragTo(endPointTemp[0], endPointTemp[1], duration=randUpDown(dragMS, floatDragMS)/1000)#拖动间隔500ms,随机浮动100ms
        i = i + 1
        sss = randUpDown(sleepSec, floatSleepSec)
        print(i, '等待', sss, 's')
        time.sleep(sss)

#随机上下浮动
def randUpDown(center, rand):
    return random.randint(center-rand, center+rand)

if __name__ == '__main__':
    time.sleep(3)
    #print(pyautogui.position())
    main()
    