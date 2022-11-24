import random
import pygame


class Bird(object):
    # 类变量
    def __init__(self):
        self.bird_Rect=pygame.Rect(110,48,48,34)
        self.BirdState = [pygame.image.load("files\images\\bird1_0.png"),
                          pygame.image.load("files\images\\bird1_1.png"),
                          pygame.image.load("files\images\\bird1_2.png"), ]
        self.state = 0
        # 默认X轴坐标
        self.Bird_X = 120
        # 默认Y轴坐标
        self.Bird_Y = 350
        # 开启跳跃
        self.jump = False
        # 小鸟跳跃高度
        self.jump_Speed = 6
        # 小鸟重力
        self.gravity = 1
        # 小鸟是否死亡
        self.dead = False


    # 小鸟移动
    def birdupdate(self):
        if self.jump:
            # 跳跃高度 越高跳的越低
            self.jump_Speed-=0.65
            self.Bird_Y-=self.jump_Speed
        else:
            self.gravity+=1
            self.Bird_Y+=self.gravity
        self.bird_Rect[1]=self.Bird_Y
            
# 管道类
class Pipe(object):
    def __init__(self):
        # 默认X轴坐标
        self.pipes_X=400
        # 上管道精灵
        self.pipe_UP=pygame.image.load("files\images\pipe_down.png")
        # 下管道精灵
        self.pipe_down=pygame.image.load("files\images\pipe_up.png")
        # 第一次管道高度为-100
        self.pipe_height=-100

    def pipeipdate(self):
        self.pipes_X-=2
        # 管道x左边为负数
        if self.pipes_X<-40:
            # global获取类之外的变量 分数加1
            global score 
            score+=1
            # 随机管道高度
            self.pipe_height=random.randint(50,270)-320
            # 管道x轴刷新 生成新的
            self.pipes_X=400


# 生成背景地图
def creaceMap():
    # 创建背景精灵
    background = pygame.image.load("files\images\\bg_day.png")
    # 放大背景图片
    background = pygame.transform.scale(background, (size))
    # 生成背景图片
    screen.blit(background, (0, 0))
    # 生成上随机管道
    screen.blit(pipe.pipe_UP,(pipe.pipes_X,pipe.pipe_height))
    # 生成下随机管道
    screen.blit(pipe.pipe_down,(pipe.pipes_X,pipe.pipe_height+580))
    # 更新管道
    pipe.pipeipdate()
    if bird.dead:
        bird.state=2
    elif bird.jump:
        bird.state=1
    screen.blit(bird.BirdState[bird.state],(bird.Bird_X,bird.Bird_Y))
    bird.birdupdate()
    # 检测分数
    score_font=font.render("分数"+ str(score),True,(255,105,180))
    screen.blit(score_font,(150,100))
    # 更新屏幕
    pygame.display.update()
# 检测是否小鸟死亡
def cheekDead():
    # 创建上管道的矩形
    upRect=pygame.Rect(pipe.pipes_X,pipe.pipe_height,pipe.pipe_UP.get_width(),pipe.pipe_UP.get_height())
    # 创建下管道的矩形
    downRect=pygame.Rect(pipe.pipes_X,pipe.pipe_height+580,pipe.pipe_down.get_width(),pipe.pipe_down.get_height())
    # 检测碰撞
    if upRect.colliderect(bird.bird_Rect) or downRect.colliderect(bird.bird_Rect):
        bird.dead=True
        return True
    if not 0<bird.bird_Rect[1]<WINDOW_H:
        bird.dead=True
        return True
    else:
        return False

# 游戏结束界面
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
# 开启游戏函数
def startgame():
    background = pygame.image.load("files\images\\bg_day.png")
    background = pygame.transform.scale(background, (size))
    startGame="点击或者按键盘开始游戏"
    over_font1=pygame.font.Font("files\\al.ttf",28)
    over_font1=over_font1.render(startGame,True,(173,255,47))
    screen.blit(background, (0, 0))
    screen.blit(over_font1,(55,300))
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
                # pygame获取键盘事件
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
            startgame()
