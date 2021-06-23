import pygame
import random
from pygame import mixer
pygame.init()

window = pygame.display.set_mode((800,500))
pygame.display.set_caption('This is my game')
icon = pygame.image.load('cat (1).png')
pygame.display.set_icon(icon)
background = pygame.image.load('back.png.png')

playerImage = pygame.image.load('cat (2).png')
playerX = 370
playerY = 400
playerChange = 0

enemy_icon = []
enemyX = []
enemyY = []
enemyChangeY = []
enemyChangeX = []
number_of_enemies = 6
for i in range(number_of_enemies):
    enemy_icon.append(pygame.image.load('poop.png'))
    enemyX.append(random.randint(24,800-24))
    enemyY.append(random.randint(24,200))
    enemyChangeX.append(+0.4)
    enemyChangeY.append(0)






knife_image = pygame.image.load('sword.png')
knife_x = 0
knife_y = 400
knife_change = 0.7
knife_state = 'ready'

def attack(x,y):
    global knife_state
    knife_state = 'attacking'
    window.blit(knife_image,[x+20,y+10])




def player(X,Y):
    window.blit(playerImage,[X, Y])

def enemy(X,Y, i):
    window.blit(enemy_icon[i],[X,Y])

def isCollison(enemyX,enemyY,knifeX,knifeY):
    distance = (((enemyX-knifeX)**2)+((enemyY-knifeY)**2))**0.5
    return distance < 27





score = 0
font = pygame.font.Font('freesansbold.ttf', 36)

def show_score(font):
    display = font.render(f'Score:{score}', True, (225,225,225))
    window.blit(display, (10,10))

backgroundSong = mixer.music.load('background.wav')
mixer.music.play(0)


def game_over():
    game_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_text = game_font.render('GAME OVER',True,(225,225,225))
    window.blit(game_over_text, [500/2-75, 500/2-75])



playing = True

while playing:

    window.fill([255, 255, 255])
    window.blit(background, [0,0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -0.5
            if event.key == pygame.K_RIGHT:
                playerChange = +0.5
            if event.key == pygame.K_SPACE:
                if knife_state == 'ready':
                    knife_x = playerX
                    lanching = mixer.Sound('laser.wav')
                    lanching.play()
                    attack(knife_x, knife_y)

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                playerChange = 0



    playerX += playerChange

    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    if knife_y <= 0:
        knife_y = 400
        knife_state = 'ready'
    if knife_state == 'attacking':
        attack(knife_x, knife_y)
        knife_y -= knife_change


    for i in range(number_of_enemies):
        enemyX[i] += enemyChangeX[i]

        if enemyY[i] > 300:
            for i in range(number_of_enemies):
                enemyX[i] = 1000
            game_over()
            break

        if enemyX[i] <=0:
            enemyChangeX[i] = +0.4
            enemyY[i] += 20
        if enemyX[i] >= 736:
            enemyChangeX[i] = -0.4
            enemyY[i] += 20

        if isCollison(enemyX[i],enemyY[i],knife_x,knife_y) ==True:
            explode = mixer.Sound('explosion.wav')
            explode.play()
            score += 1
            enemyX[i] = random.randint(24, 800 - 24)
            enemyY[i] = random.randint(24, 200)
            knife_y = 400
            knife_state = 'ready'

        enemy(enemyX[i], enemyY[i], i)


    player(playerX, playerY)
    show_score(font)
    pygame.display.update()
