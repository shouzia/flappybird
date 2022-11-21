import random
import pygame


class Bird(object):
    # 类变量
    def __init__(self):
        self.bird_Rect=pygame.Rect(110,48,48,34)
        self.BirdState = [pygame.image.load("files\images\\bird1_0.png")   ,
                          pygame.image.load("files\images\\bird1_1.png"),
                          pygame.image.load("files\images\\bird1_2.png"), ]
        self.state = 0
        self.Bird_X = 120
        self.Bird_Y = 350
        self.jump = False
        self.jump_Speed = 6
        self.gravity = 0
        self.dead = False


    # 小鸟移动
    def birdupdate(self):
        if self.jump:
            self.jump_Speed-=0.9
            self.Bird_Y-=self.jump_Speed
        else:
            # self.gravity+=0.1
            self.Bird_Y+=self.gravity
        self.bird_Rect[1]=self.Bird_Y
            
# 管道类
class Pipe(object):
    def __init__(self):
        self.pipes_X=400
        self.pipe_UP=pygame.image.load("files\images\pipe_down.png")
        self.pipe_down=pygame.image.load("files\images\pipe_up.png")
        self.pipe_height=-100

    def pipeipdate(self):
        self.pipes_X-=2
        if self.pipes_X<-40:
            # global获取类之外的变量
            global score
            score+=1
            self.pipe_height=random.randint(100,320)-320
            self.pipes_X=400


# 生成背景地图
def creaceMap():
    background = pygame.image.load("files\images\\bg_day.png")
    background = pygame.transform.scale(background, (size))
    screen.blit(background, (0, 0))
    screen.blit(pipe.pipe_UP,(pipe.pipes_X,-100))
    screen.blit(pipe.pipe_down,(pipe.pipes_X,400))
    pipe.pipeipdate()

    if bird.dead:
        bird.state=2
    elif bird.jump:
        bird.state=1
    
    screen.blit(bird.BirdState[bird.state],(bird.Bird_X,bird.Bird_Y))
    bird.birdupdate()
    
    score_font=font.render("分数"+ str(score),True,(255,105,180))
    screen.blit(score_font,(150,100))
    # 更新屏幕
    pygame.display.update()

def cheekDead():
    upRect=pygame.Rect(pipe.pipes_X,-100,pipe.pipe_UP.get_width(),pipe.pipe_UP.get_height())
    downRect=pygame.Rect(pipe.pipes_X,400,pipe.pipe_down.get_width(),pipe.pipe_down.get_height())
    if upRect.colliderect(bird.bird_Rect) or downRect.colliderect(bird.bird_Rect):
        bird.dead=True
        return True
    if not 0<bird.bird_Rect[1]<WINDOW_H:
        bird.dead=True
        return True
    else:
        return False


def getResult():
    text1="游戏结束"
    text2="你的得分是"+str(score)
    over_font1=pygame.font.Font("files\\al.ttf",50)
    over_font1=over_font1.render(text1,True,(174,255,0))
    over_font2=pygame.font.Font("files\\al.ttf",50)
    over_font2=over_font2.render(text2,True,(174,255,0))
    screen.blit(over_font1,(95,150))
    screen.blit(over_font2,(70,250))
    pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    # 初始化游戏字体
    font=pygame.font.Font("files\\al.ttf",30)
    # 游戏窗口的大小
    size = WINDOW_W, WINDOW_H = 400, 650
    # 每秒的帧数
    FPS = 60
    #游戏是否开始判断
    flag=False 
    # 窗口大小
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    # 设置窗口名字
    pygame.display.set_caption("Flapp-Bird")
    # 实例化时钟
    clock = pygame.time.Clock()
    
    # 实例化鸟
    bird=Bird()
    # 实例化管道
    pipe=Pipe()
    # 随机管道高度
    
    # 分数
    score=0
    
    while True:
        # 设置游戏的刷新利
        clock.tick(FPS)
        # 事件触发
        for event in pygame.event.get():
            # 检测点击关闭关闭窗口
            if event.type == pygame.QUIT:
                quit()
            if event.type==pygame.MOUSEBUTTONUP or event.type==pygame.KEYUP and not bird.dead:
                bird.jump=True
                bird.gravity=5
                bird.jump_Speed=10
                # 游戏开始
                flag=True
                
        if flag:
            if cheekDead():
                getResult()
            else:
                creaceMap()
                bird.jump=True
        else:
            background = pygame.image.load("files\images\\bg_day.png")
            background = pygame.transform.scale(background, (size))
            startGame="点击或者按键盘开始游戏"
            over_font1=pygame.font.Font("files\\al.ttf",28)
            over_font1=over_font1.render(startGame,True,(174,255,0))
            screen.blit(background, (0, 0))
            screen.blit(over_font1,(55,150))
            pygame.display.update()
