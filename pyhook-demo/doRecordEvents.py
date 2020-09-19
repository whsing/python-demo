# coding=utf-8
import pyautogui, json, time

def moveMouse(p,delay=0):
    pyautogui.moveTo(p[0],p[1],duration=delay)

def doRecordEvents():
   with open("recordEvents.txt","r") as file:
      events = json.loads(file.read())
      #print(json.dumps(events,indent=2))
   
   lastTime = 0
   delay = 0
   first = True
   for e in events:
      MessageName = e.get("MessageName")
      Position = e.get("Position")
      Time = e.get("Time")
      
      if first:
         first = False
      else:
         delay = Time - lastTime
      
      lastTime = Time
      delay = float(delay) / 1000 / 4
      print(json.dumps(e))
      print("delay:" + str(delay))
      if MessageName == "mouse left down":
         moveMouse(Position, delay)
         pyautogui.mouseDown()
      if MessageName == "mouse left up":
         moveMouse(Position, delay)
         pyautogui.mouseUp()
      if MessageName == "mouse right down":
         moveMouse(Position, delay)
         pyautogui.mouseDown(button="right")
      if MessageName == "mouse right up":
         moveMouse(Position, delay)
         pyautogui.mouseUp(button="right")
      if MessageName == "mouse wheel":
         moveMouse(Position, delay)
         pyautogui.scroll(e.get("wheel"))

if __name__ == "__main__":
  doRecordEvents()