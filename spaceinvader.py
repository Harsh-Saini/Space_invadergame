import pygame
import random
import math
from pygame import mixer

pygame.init()

# game window
screen = pygame.display.set_mode((800, 600))

# game window icon and title
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invader",)

# background image
background = pygame.image.load('background.png')
# background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# player
player_img = pygame.image.load('spaceship.png')
playerX = 370
playerY = 520
playerX_change = 0

# enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(10, 90))
    enemyX_change.append(4)
    enemyY_change.append(20)

# bullet
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 520
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('funSized.ttf', 32)

textX = 10
textY = 10

# game over
game_over_font = pygame.font.Font('GoSpeeds.ttf', 100)


def game_over_text():
    game_over = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (250, 220))


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+16, y+10))


def check_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance <= 27:
        return True
    else:
        return False


running = True

while running:
    screen.fill((208, 129, 155))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            if event.key == pygame.K_RIGHT:
                playerX_change = 8
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX >= 730:
        playerX = 730
    elif playerX <= 10:
        playerX = 10

    for i in range(number_of_enemies):
        if enemyY[i] > 470:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] >= 730:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] <= 10:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]

        collision = check_collision(enemyX[i], enemyY[i], bulletX, bulletY)

        if collision:
            bulletY = 520
            bullet_state = "ready"
            hit_Sound = mixer.Sound('explosion.wav')
            hit_Sound.play()
            score_value += 1
            enemyX[i] = random.randint(0, 730)
            enemyY[i] = 10

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 520
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
