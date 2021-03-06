import random
import pygame
 
# 初始化 
panel_width = 600
panel_highly = 500
font_px = 15
 
pygame.init()
 
# 创建一个可视窗口
winSur = pygame.display.set_mode((panel_width, panel_highly))
font = pygame.font.SysFont("123.ttf", 25)
bg_suface = pygame.Surface((panel_width, panel_highly), flags=pygame.SRCALPHA)
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0, 0, 0, 28))
winSur.fill((0, 0, 0))
 
# 数字版
# texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]
 
# 字母版
letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
          'v', 'b', 'n', 'm']
texts = [font.render(str(letter[i]), True, (0, 255, 0)) for i in range(26)]
 
# 按屏幕的宽计算可以在画板上放几列坐标，并生成一个列表
column = int(panel_width / font_px) 
drops = [0 for i in range(column)]
 
while True:
    # 获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
 
            chang = pygame.key.get_pressed()
            if(chang[32]):
                exit()
 
    # 暂停5秒
    pygame.time.delay(30)
 
    # 重新编辑图像第二个参数是左上角の坐标
    winSur.blit(bg_suface, (0, 0))
 
    for i in range(len(drops)):
        text = random.choice(texts)
 
        # 重新编辑每个坐标点的图像
        winSur.blit(text, (i * font_px, drops[i] * font_px))
 
        drops[i] += 1
        if drops[i] * 10 > panel_highly or random.random() > 0.95:
            drops[i] = 0
 
    pygame.display.flip()
