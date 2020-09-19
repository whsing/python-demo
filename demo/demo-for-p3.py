# -*- coding: utf-8 -*-
import pyautogui
import time
from PIL import ImageGrab
import requests
import json  

image = ImageGrab.grab()
#各按钮位置
back = (1172,79)    #返回按钮 位置
yes = (1520,780)    #下一步、购买、预定 位置
chooseall = (1182,556)    #全选 位置
payway = (1348,499)    #深圳通 位置
firstDay = (1245,271)    #第一行第二个 位置
startDay = (1,0)    #去除两边两列，其余作为二维数组，这里表示从哪个开始

#配置参数
SLEEP_TIME = 5   #每次查询一次间隔，秒
MOVE_DELAY = 0.7 #鼠标移动快慢

def moveMouse(p,delay=MOVE_DELAY):
    pyautogui.moveTo(p[0],p[1],duration=MOVE_DELAY)
    return
def moveMouseAndClick(p):
    moveMouse(p)
    pyautogui.leftClick()
    return

access_token_dict = "CiVtys2uaX5bhoN1neLW6ltmJcZSGvEFdS6gKYc5S0YBjCA3yxNpn08H_ZRTc8yPz7M5NFwGbjrpjrhufytxcsDouOz717rDnaycumXdg5R-Rs2FFQ2B5Pg00GHxnVdl0TZ2IFFnCa7W4c262q2MTsw3pR5exEHvVK_hmGgeKQbuxNZQ3GpIkQZi1zKjWO3e7aY0puGBNq8AfnpAU4fMzA"
def getAccessTokenOnline():
    url_get_access_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww6ad44f5ad7e43960&corpsecret=xeTjchpO7aFljCMq8TpiXrYWTuVgCDvtZARm0_7Y8AQ"
    response = requests.get(url_get_access_token)
    jsonObj = json.loads(response.text)
    errcode = jsonObj["errcode"]
    if errcode != 0 :
        print ("errorcode： getAccessTokenOnline()")
        print (response.text)
    else :
        access_token_dict = jsonObj["access_token"]
    return access_token_dict
def sendWxWorkMsg(content,agentid,access_token):
    base_url_post_msg = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="
    payload = json.dumps({
        "touser" : "wuxinglin",
        "msgtype" : "text",
        "agentid" : agentid,
        "text" : {
            "content" : content
        },
        "safe":0,
        "enable_id_trans": 0
    })
    response = requests.post(base_url_post_msg+access_token,data=payload)
    jsonObj = json.loads(response.text)
    errcode = jsonObj["errcode"]
    if errcode != 0 :
        getAccessTokenOnline()
        response = requests.post(base_url_post_msg+access_token,data=payload)
        jsonObj = json.loads(response.text)
        errcode = jsonObj["errcode"]
        if errcode != 0 :
            print ("***errcode: sendWxWorkMsg()")
            print (response.text)
    return response
def clickChooseDay(d):
    #moveMouseAndClick()
    return 

i=0
while (True):
    #首界面为日期页面
    test = 0
    if test == 0 :
        i += 1
        print ("attempt: " + str(i))
        moveMouseAndClick(back)
        moveMouseAndClick(yes)
        moveMouseAndClick(chooseall)#选择
        color = ImageGrab.grab().getpixel(yes)
        moveMouseAndClick(yes)  #购买
        time.sleep(0.5)
        color2 = ImageGrab.grab().getpixel((yes[0]+10,yes[1]))
        if color != color2 :
            moveMouseAndClick(payway)
            time.sleep(0.5)
            moveMouse(yes)
            sendWxWorkMsg("Bought it...", 1000014, access_token_dict)
            print ("Bought it.................")
        time.sleep(SLEEP_TIME)
    else:
        sendWxWorkMsg("测试",1000014, access_token_dict)
        #sendWxWorkMsg("测试",1000027, "Zkxr7kgvtVmUl7tVqlnCA9nkF0ebXleoDJlbjqIek9I5fg9y7nezEQhP_UWjzDw7HDSGB4ch54S5ejMfErjK3-6CO1Kah1Iu01HUkNrgx9_wZdxflDClCD0C0DpBkIQjL-3RkAwRyGZH31iWKo3Imup1ovpH41azLY1qHOTEFgg8MEOkUl8_-glJM8Aj_Rv3qKAKygrZnYzdmNAN5kmlnw")
        break
