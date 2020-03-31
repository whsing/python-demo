import pygame,sys,time,random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
displaySize = (480, 640)
playSurface = pygame.display.set_mode(displaySize)
pygame.display.set_caption('打飞机')

whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)
redColor = pygame.Color(245, 69, 69)

enemyHeight = 20    #敌机大小
enemyMovePX = 1    #敌机一次移动距离
enemyMoveHz = 100     #移动频率
myHeight = 40   #我方大小
bulletHeight = 3    #子弹大小
bulletMovePX = 5   #子弹一次移动距离

enemyPlane = [] #敌机
bullets = [] #子弹

seq = 1     #敌机生成的自加值
randSeq = 0     #敌机随机次数，达到此次数生成飞机
bulletSeq = 1   #子弹生成的自加值
suspend = False #是否暂停

def quit():
    time.sleep(3)
    pygame.quit()
    sys.exit()

while True:
    #print(time.gmtime().tm_sec)
    for event in pygame.event.get():
        if event.type == QUIT:  #退出
            quit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:    #空格暂停
                suspend = False if suspend else True
                
    if suspend:
        #暂停
        pygame.mouse.set_visible(True)
        continue
    else: pygame.mouse.set_visible(False)
    
    #生成敌机
    if len(enemyPlane) == 0 or randSeq == seq:
        seq = 1
        randSeq = random.randint(20,(enemyHeight + myHeight) / enemyMovePX)
        enemyPlane.append([random.randint(0, 480-enemyHeight), 0.0])
    else:
        seq += 1
    
    #我方飞机，跟踪鼠标
    myPos = pygame.mouse.get_pos()
    myPos = (min(myPos[0], displaySize[0]-myHeight), min(myPos[1],  displaySize[1]-myHeight))
    #生成子弹
    if bulletSeq == 20:
        bulletSeq = 1
        bullets.append([int(myPos[0] + myHeight/2), myPos[1]])
    else:
        bulletSeq += 1
    
    #检测是否2机碰撞
    for enemy in enemyPlane:
        for bullet in bullets:
            if bullet[1] <= 0:
                bullets.remove(bullet)
                continue
            elif enemy[0] - bulletHeight < bullet[0] < enemy[0] + enemyHeight and enemy[1] - bulletHeight < bullet[1] < enemy[1] + enemyHeight:
                enemyPlane.remove(enemy)
                bullets.remove(bullet)
            elif enemy[1] > 640 and enemy in enemyPlane:
                enemyPlane.remove(enemy)
            elif myPos[0] - enemyHeight < enemy[0] < myPos[0] + myHeight and myPos[1] - enemyHeight < enemy[1] < myPos[1] + myHeight:
                circleCenter = [0, 0]
                #撞击的点left
                if enemy[0] < myPos[0]:
                    circleCenter[0] = int((enemyHeight + myPos[0] + enemy[0]) / 2)
                elif enemy[0] > myPos[0] + myHeight - enemyHeight:
                    circleCenter[0] = int((myHeight + myPos[0] + enemy[0]) / 2)
                else:
                    circleCenter[0] = int(enemy[0] + enemyHeight / 2)
                #撞击的点top
                if enemy[1] < myPos[1]:
                    circleCenter[1] = int((enemyHeight + myPos[1] + enemy[1]) / 2)
                elif enemy[1] > myPos[1] + myHeight - enemyHeight:
                    circleCenter[1] = int((myHeight + myPos[1] + enemy[1]) / 2)
                else:
                    circleCenter[1] = int(enemy[1] + enemyHeight / 2)
                #撞击效果，绘制圆
                pygame.draw.circle(playSurface, redColor, circleCenter, 5)
                pygame.display.update()
                quit()
            
    playSurface.fill(whiteColor)
    
    #绘制敌机
    for index,enemy in enumerate(enemyPlane):
        enemyPlane[index] = [enemy[0], enemy[1] + enemyMovePX]
        pygame.draw.rect(playSurface, blackColor, Rect(enemyPlane[index], (enemyHeight, enemyHeight)))
    #绘制子弹
    for index,bullet in enumerate(bullets):
        bullets[index] = [bullet[0], bullet[1] - bulletMovePX]
        pygame.draw.circle(playSurface, blackColor, bullets[index], bulletHeight)
    #绘制我机
    pygame.draw.rect(playSurface, blackColor, Rect(myPos, (40, 40)))

    #透明块
    '''
    s = pygame.Surface((50,50))
    s.fill(redColor)
    s.set_alpha(75)
    playSurface.blit(s,(0,0))
    '''
    
    pygame.display.update()
    fpsClock.tick(enemyMoveHz)
    
