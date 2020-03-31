import pygame, sys, time, random
from pygame.locals import *

#初始化pygame
pygame.init()
fpsClock = pygame.time.Clock()  #设定一个时钟

playSurface = pygame.display.set_mode((640, 480))   #设置窗口
pygame.display.set_caption('贪吃蛇!')  #窗口标题
image = pygame.image.load('SnakeGo.ico')    #图标
pygame.display.set_icon(image)
#一些颜色
redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)
greyColor = pygame.Color(150,150,150)
lightGery = pygame.Color(220,220,220)
#开始、退出按钮位置
buttonStartPos = [150, 300]
buttonQuitPos = [390, 300]
commonFontName = 'SimHei'   #内置字体名
commonFont = pygame.font.SysFont(commonFontName,18) #通用字体
#背景黑色
playSurface.fill(blackColor)
buttonImage = pygame.image.load('btn.jpg')  #加载按钮背景，此处为图片
pygame.display.flip()

num = 0         #全局试玩次数
maxScore = 0    #最高分
score = 0       #当前分

#退出游戏
def quit():
    pygame.quit()
    sys.exit()
#显示按钮，刚开始和游戏结束都显示
def showBtn():
    #绘制按钮图片背景
    playSurface.blit(buttonImage, buttonStartPos)
    playSurface.blit(buttonImage, buttonQuitPos)

    #绘制文字
    if num == 0:
        startSurf = commonFont.render('开始', True, blackColor)
        startRect = startSurf.get_rect()
        startRect.topleft = (buttonStartPos[0]+30,buttonStartPos[1]+5)
        playSurface.blit(startSurf, startRect)
    else:
        startSurf = commonFont.render('重新开始', True, blackColor)
        startRect = startSurf.get_rect()
        startRect.topleft = (buttonStartPos[0]+15,buttonStartPos[1]+5)
        playSurface.blit(startSurf, startRect)
    
    quitSurf = commonFont.render('退出', True, blackColor)
    quitRect = quitSurf.get_rect()
    quitRect.topleft = (buttonQuitPos[0]+33,buttonQuitPos[1]+5)
    playSurface.blit(quitSurf, quitRect)

def welcome():
    welcomeFont = pygame.font.SysFont(commonFontName,60)
    welcomeSurf = welcomeFont.render('欢迎来玩贪吃蛇', True, greyColor)
    welcomeRect = welcomeSurf.get_rect()
    welcomeRect.midtop = (320,125)
    playSurface.blit(welcomeSurf, welcomeRect)
    
    showBtn()
#游戏失败动作    
def gameOver(score):
    print('call gameOver().')
    print('次数:' + str(num) + ', 最高分:' + str(maxScore))
    if score > maxScore:
        global  maxScore
        maxScore = score
        commonFontName,72
   
    gameOverFont = pygame.font.SysFont(commonFontName,72)
    gameOverSurf = gameOverFont.render('游戏结束', True, greyColor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320,125)
    playSurface.blit(gameOverSurf, gameOverRect)
    
    scoreFont = pygame.font.SysFont(commonFontName,48)
    scoreSurf = scoreFont.render('分数: ' + str(score), True, greyColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (320,225)
    playSurface.blit(scoreSurf,scoreRect)
    
    showConstantInfo()
    showBtn()
    pygame.display.flip()
    
def showConstantInfo():    
    scoreFont = pygame.font.SysFont(commonFontName,17)
    scoreSurf = scoreFont.render('次数:' + str(num) + ', 最高分:' + str(maxScore), True, greyColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (10,10)
    #抹去第一行字，相当于刷新此区域
    pygame.draw.rect(playSurface, blackColor, Rect(scoreRect.left, scoreRect.top, scoreRect.width, scoreRect.height))
    playSurface.blit(scoreSurf,scoreRect)

    scoreSurf = scoreFont.render('得分:' + str(score), True, greyColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (10,30)
    playSurface.blit(scoreSurf,scoreRect)

    pygame.display.flip()
#一局游戏主体
def start():
    #重置游戏参数
    snakePosition = [100, 100]  #蛇开始的位置
    snakeSegments = [[100, 100], [80, 100], [60, 100]]  #蛇身体
    raspberryPosition = [200, 100]  #草莓初始位置
    raspberrySpawned = 1    #草莓个数
    direction = 'right' #初始方向
    changeDirection = direction     #需要改变的方向
    global score
    score = 0

    global num
    num += 1
    
    while True:
        #监控事件
        for event in pygame.event.get():
            if event.type == QUIT:  #退出
                print('press esc (QUIT)')
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: #按下键
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        #不能反向
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection
        #移动蛇身体
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20
        #移动后的新位置插入到首部
        snakeSegments.insert(0, list(snakePosition))
        #判断是否吃到草莓
        if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
            raspberrySpawned = 0    #吃到
        else:
            snakeSegments.pop() #没吃到，删除尾部
        #生成一个随机位置草莓
        if raspberrySpawned == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            raspberryPosition= [int(x*20), int(y*20)]
            raspberrySpawned = 1
            score += 1
        
        playSurface.fill(blackColor)
        #绘制蛇身
        for position in snakeSegments[1:]:
            pygame.draw.rect(playSurface, lightGery , Rect(position[0], position[1], 20, 20))
        #绘制蛇头
        pygame.draw.rect(playSurface, whiteColor, Rect(snakePosition[0], snakePosition[1], 20, 20))
        #绘制草莓
        pygame.draw.rect(playSurface, redColor, Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
        showConstantInfo()
        pygame.display.update()
        #判断是否触碰到墙、自身
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            print('碰墙')
            gameOver(score)
            break
        if snakePosition[1] > 460 or snakePosition[1] < 0:
            print('碰墙')
            gameOver(score)
            break
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                print('碰到自己')
                gameOver(score)
                break
        #逐渐提高速度（难度），到一定程度不再提高
        if len(snakeSegments) < 40:
            speed = 6 + len(snakeSegments)//4
        else:
            speed = 16
        fpsClock.tick(speed)

def listenStart():
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                quit()
            elif e.type == pygame.MOUSEBUTTONDOWN and buttonStartPos[0] <= e.pos[0]<=100+buttonStartPos[0] and buttonStartPos[1]<=e.pos[1] <= 30+buttonStartPos[1]:
                start()
            elif e.type == pygame.MOUSEBUTTONDOWN and buttonQuitPos[0] <= e.pos[0]<=100+buttonQuitPos[0] and buttonQuitPos[1]<=e.pos[1] <= 30+buttonQuitPos[1]:
                quit()

if __name__ == '__main__':
    welcome()
    pygame.display.flip()
    listenStart()
    

