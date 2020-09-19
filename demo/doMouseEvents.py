# -*- coding: utf-8 -*-
import pyautogui,time
from PIL import ImageGrab
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import requests
import json

pyautogui.FAILSAFE = True   #移动到左上角自动退出

k = PyKeyboard()
m = PyMouse()

image = ImageGrab.grab()
#自动添加李总授权，除公益、基金会
#各按钮位置
p1 = (1186,150)    #添加
p2 = (966, 294)    #选择
p3 = (980, 367)    #具体到人
p4 = (1079, 330)    #选人按钮
p5 = (458, 361)    #搜索框文本框
p6 = (517, 357)    #查询框
p7 = (382, 388)  #第一条人员位置 此处要双击
p8 = (661, 602)  #确定选人
p9 = (984, 366)  #公司发起，
p10 = (1073, 423) #选择公司按钮
p11 = (447, 186)  #展开公司第一级
p12 = (700, 454)  #弹窗，为了拉大网页
p13 = (526, 183)  #集团公司的位置
p14 = (893, 488)    #保存的位置
p15 = (1123, 486)   #下拉箭头
#comSeqs = (3,4,5,6,8,10,11,12,13,14,15,16) #需要选中的公司，循环每次双击
comSeqs = (10,11,12,13,14,15,16) #需要选中的公司，循环每次双击

#配置参数
SLEEP_TIME = 5   #每次查询一次间隔，秒
MOVE_DELAY = 0.5 #鼠标移动快慢

def moveMouse(p,delay=MOVE_DELAY):
    pyautogui.moveTo(p[0],p[1],duration=MOVE_DELAY)
    return
def moveMouseAndClick(p,delay=MOVE_DELAY):
    moveMouse(p,delay)
    pyautogui.leftClick()
    return
def moveMouseAndDoubleClick(p,delay=MOVE_DELAY):
    moveMouse(p,delay)
    pyautogui.doubleClick()
    return

i=0
for comSeq in comSeqs:
    moveMouseAndClick(p1)
    moveMouseAndClick(p2, 2)
    moveMouseAndClick(p3)
    moveMouseAndClick(p4)
    moveMouseAndClick(p5, 5)
    k.type_string('100093')
    moveMouseAndClick(p6)
    moveMouseAndDoubleClick(p7,5)
    moveMouseAndClick(p8)
    moveMouseAndClick(p9)
    moveMouseAndClick(p10)
    pyautogui.moveTo(p12[0],p12[1])
    pyautogui.dragRel(50, 50)
    moveMouseAndClick(p11,5)
    moveMouseAndDoubleClick((p13[0], p13[1]+(comSeq*18)))
    moveMouseAndClick(p15)
    moveMouseAndClick(p14)
    #break
