import pygame
import os
import random

pygame.init()

window = pygame.display.set_mode((500, 500))
bullet=pygame.transform.scale(pygame.image.load(os.path.join("assets", "bullet.png")),(100,60))
player=pygame.transform.scale(pygame.image.load(os.path.join("assets", "player.png")),(100,60))
enemy=pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy.png")),(100,60))
explode=pygame.transform.scale(pygame.image.load(os.path.join("assets", "explode.png")),(100,60))
life=3
font1 = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 25)
endtext = font1.render('You Lose', True,(0,0,128))




x = 250
y = 390
vel = 5
bulletX = 250
bulletY = 390
bulletV=15
enemyX=250
enemyY=0
enemyV=5
explodeX=250
explodeY=0
score=0
shoot= False
collide=False
run = True


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0:
        x -= vel
        if not shoot:
            bulletX -= vel
    if keys[pygame.K_RIGHT] and x<410:
        x += vel
        if not shoot:
            bulletX += vel
    if keys[pygame.K_SPACE]:
        shoot=True
    if(bulletY<-10):
        bulletY=y
        bulletX=x
        shoot=False
    if(bulletX>=enemyX-28 and bulletX<=enemyX+20 and bulletY<=enemyY):
        collide=True
        explodeX = enemyX
        explodeY = enemyY
        enemyX= random.randrange(50,420)
        enemyY=0
        score+=10
    if(enemyY>=410):
        enemyY=0
        life-=1
    lifetext = font2.render(('Lives: '+(str(life))), True, (255, 255, 255))
    scoretext = font2.render(('Score: '+str(score)), True, (255, 255, 255))


    if(life>0):
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 0, 0), (0, 450, 500, 2), 2)
        window.blit(bullet,(bulletX,bulletY))
        window.blit(player,(x,y))
        window.blit(lifetext,(10,15))
        window.blit(scoretext,(200,475))
        if shoot:
            bulletY-=bulletV
        if not collide:
            window.blit(enemy,(enemyX,enemyY))
            enemyY+=enemyV
        if collide:
            window.blit(explode,(explodeX,explodeY))
            window.blit(enemy,(enemyX,enemyY))
            collide=False

        pygame.display.update()
    if(life<=0):
        window.fill((0, 0, 0))
        window.blit(endtext,(180,250))
        pygame.display.update()


pygame.quit()
