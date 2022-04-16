from email import message
from re import X
from tkinter import Y
import pygame

FONT_PATH = "lumberjack/HigashiOme-Gothic-1.3i.ttf"

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255,255,255))

pygame.display.set_caption('Lumberjack Game')

# Variable to keep the main loop running
running = True

playerX = 200
playerY = 270
strike_num = 0
attack_value = 2
damage_value = strike_num * attack_value
endurance_value = 10000

def player(x, y):
    screen.blit(playerImg, (x,y))

playerImg = None

while running:# イベントハンドラーの開始
    screen.fill((255,255,255))
    #文字
    font =  pygame.font.Font (FONT_PATH, 50)
    message = font.render('kikorin', False, (0,0,0))
    screen.blit(message, (20, 50))

    font = pygame.font.SysFont(None, 20)
    zahyo = 'playerX=' + str(playerX) + '   ' + 'playerY=' + str(playerY)
    message2 = font.render(zahyo, False, (0,0,0))
    screen.blit(message2, (20, 100))

    # strike_num
    font =  pygame.font.Font (FONT_PATH, 30)
    str_strike_num = '叩いた回数 : ' + str(strike_num)
    strike_num_text = font.render( str_strike_num , False, (0,0,0))
    screen.blit(strike_num_text, (20, 150))
    
    # damage_value
    font =  pygame.font.Font (FONT_PATH, 30)
    str_damage_value = '木に与えたダメージ : ' + str(damage_value)
    damage_value_text = font.render( str_damage_value , False, (0,0,0))
    screen.blit(damage_value_text, (20, 200))

    # endurance_value
    font =  pygame.font.Font (FONT_PATH, 20)
    str_endurance_value = '耐久値 : ' + str(endurance_value)
    endurance_value_text = font.render( str_endurance_value , False, (0,0,0))
    screen.blit(endurance_value_text, (20, 250))

    if damage_value < endurance_value :
        #読み込み
        treeImg = pygame.image.load("lumberjack/tree.jpeg")
        #大きさ指定
        treeImg = pygame.transform.scale(treeImg, (130, 130))
        #画像中心
        treeImg_center = (
            (SCREEN_WIDTH-treeImg.get_width())/2,
            (SCREEN_HEIGHT-treeImg.get_height())/2
        )
        #画像表示
        screen.blit(treeImg, treeImg_center)
    elif damage_value >= endurance_value :
        pass

    

    #読み込み
    playerImg2 = pygame.image.load("lumberjack/man3.png")
    #大きさ指定
    playerImg2 = pygame.transform.scale(playerImg2, (130, 130))

    #読み込み
    playerImg1 = pygame.image.load("lumberjack/man.png")
    #大きさ指定
    playerImg1 = pygame.transform.scale(playerImg1, (130, 130))

    #移動
    if playerX < 270:
        playerImg = playerImg1
        playerX += 1
    elif playerX == 270 and damage_value >= endurance_value :
        screen.fill((255,255,0))

        #完了のメッセージ
        font =  pygame.font.Font (FONT_PATH, 30)
        str_complete_text = 'こんなに大きな木でも'+ str(strike_num) +'回叩けば倒れます。'
        complete_text = font.render( str_complete_text , False, (0,0,0))
        screen.blit(complete_text, (20, 100))

        str_complete_text = 'この木の耐久値 : '+ str(endurance_value)
        complete_text = font.render( str_complete_text , False, (0,0,0))
        screen.blit(complete_text, (20, 150))
        str_complete_text = '斧のパワー : ' + str(attack_value)
        complete_text = font.render( str_complete_text , False, (0,0,0))
        screen.blit(complete_text, (20, 200))
        
        pass
    elif playerX == 270:
        playerImg = playerImg2
        strike_num += 1
        damage_value = strike_num * attack_value

        

    

    # 停止
    player(playerX,playerY)


    # 木に近づいたら木こり動き出す
    # if im
    # 動くとともに叩いた回数に+1


    playerImg_change =0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    
    pygame.display.update()