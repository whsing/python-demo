# -*- coding:utf-8 -*-
import pythoncom
import pyHook, time, os

events = []
pause = False
def onMouseEvent(event):
   global pause
   if event.MessageName.find("mouse middle") >= 0:
      if event.MessageName == "mouse middle up":
         if pause:
            pause = False
            print("按下了中间键-->开始")
         else:
            pause = True
            print("按下了中间键-->暂停")
      return True
   
   if not pause and event.MessageName != "mouse move":
      print ("MessageName:",event.MessageName)
      print ("Message:", event.Message)
      print ("Time:", event.Time)
      # print ("Window:", event.Widow)
      print ("WindowName:", event.WindowName)
      print ("Position:", event.Position)
      print ("Wheel:", event.Wheel)
      print ("Injected:", event.Injected)
      print("---")
      
      events.append(event)
   
   return True
if __name__ =="__main__":
    # 命令行改为utf-8显示模式
    os.system("chcp 65001")
    
    #mykbmanager = KeyBoardManager()
    # 创建一个“钩子”管理对象
    hookmanager = pyHook.HookManager()
    #监控键盘操作
    #hookmanager.KeyDown= mykbmanager.onKeyDown
    #hookmanager.KeyUp = mykbmanager.onKeyUp
    # 设置键盘“钩子”
    #hookmanager.HookKeyboard()
 
    #监控鼠标操作
    hookmanager.MouseAll = onMouseEvent
    # 设置鼠标“钩子”
    hookmanager.HookMouse()
 
    # 循环获取信息
    pythoncom.PumpMessages()