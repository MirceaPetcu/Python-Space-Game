import pygame
import math
pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('Space Game')
running = False
clock = pygame.time.Clock()

#IMBUNATATIRI
def distanta_boom_fct(x1,y1,x2,y2):
    d = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    return d
red = (255,0,0)
blue = (0,200,255)
a = 0
def draw_life_fct(a):
    pygame.draw.rect(dis,red,[150,10,a*10,10])
def full_life_fct():
    pygame.draw.rect(dis,blue,[150,10,200,10])

lost = 0

#boss
boss1_img = pygame.image.load('monster.png')
boss1x = 300
boss1y = 100
def boss1_fct(x,y):
    dis.blit(boss1_img,(x,y))

DAMAGE1 = 0
nr_inc = 0





#text
black =(0,0,0)
system_fonts = pygame.font.SysFont('calibri', 64)
system_text = system_fonts.render('YOU WON!',True,black)
system_text2 = system_fonts.render('YOU LOST!',True,black)
OK = 0
system_fonts = pygame.font.SysFont('calibri', 20)
system_text3 = system_fonts.render('LIFE: ',True,black)
score = 0
ok_lost = 0
def score_fct(score):
    score_text = system_fonts.render(score, True, black)
    dis.blit(score_text,(20,20))
def text_fct(x,y):
    global OK
    OK = 1
    dis.blit(system_text,(x,y))

def text2_fct(x,y):
    global ok_lost
    dis.blit(system_text2,(x,y))
    ok_lost = 1
def text3_fct(x,y):
    dis.blit(system_text3,(x,y))
#player
player_image = pygame.image.load('spaceship.png')
playerx = 400
playery= 530
x = 400
y = 500
x_change = 0

def player_fct(x,y):
        dis.blit(player_image,(x,y))



#alien
alien_image = pygame.image.load('ufo.png')
alien_vectx = [23,500,89,400,130,300]
alien_vecty = [23,50,80,120,150,180]

xa_change = [8,8,8,8,8,8]
ok = 0
def alien_fct(x,y):
      global iscollision_v
      if iscollision_v[i] is False:
          dis.blit(alien_image,(x,y))

bullet_alien_img = pygame.image.load('laser.png')
bullet_alien_vectx = [alien_vectx[0], alien_vectx[1], alien_vectx[2], alien_vectx[3], alien_vectx[4], alien_vectx[5]]
bullet_alien_vecty = [alien_vecty[0], alien_vecty[1], alien_vecty[2], alien_vecty[3], alien_vecty[4], alien_vecty[5]]
bullet_alien_status = 'ready'
def bullet_alien_fct(x,y):
    global bullet_alien_status
    bullet_alien_status = 'fire'
    dis.blit(bullet_alien_img, (x+8, y+5))



#bullet
bullet_image = pygame.image.load('bullet (1).png')
bulletx = playerx
bullety = playery
bullets = 'ready'
nr_bullets = 0
def bullet_foc(x,y):
    global bullets,nr_bullets
    if nr_bullets <= 30:
        bullets ='fire'
        dis.blit(bullet_image,(x+16,y+10))

#bombaplayer
bomba_img = pygame.image.load('explosion (1).png')
bombax = playerx
bombay = playery
def explosion_player_fct(x,y):
    dis.blit(bomba_img,(x+16,y+10))


#bomb_and_bullet_boss
bomba_boss_img = pygame.image.load('explosion (1).png')
bullet_boss_img = pygame.image.load('nuclear-bomb.png')
bullet_boss1x = boss1x
bullet_boss1y = boss1y
bullet_boss1_status = 'ready'
bossx_change = 6

def explosion_boss_fct(x,y):
    dis.blit(bomba_boss_img,(x,y+125))

def bullet_boss1_fct(x,y):
    global bullet_boss1_status, bullet_boss1y
    if bullet_boss1y != 2000 and bullet_boss1x != 2000:
        bullet_boss1_status = 'fire'
        dis.blit(bullet_boss_img,(x+55,y+125))
        dis.blit(bullet_boss_img, (x , y+125 ))
        dis.blit(bullet_boss_img, (x + 100, y + 125))

big_explosion_boss_img = pygame.image.load('explosion_boss.png')
def big_explosion_boss_fct(x,y):
    dis.blit(big_explosion_boss_img,(x,y))

#bumba
bumba_img = pygame.image.load('explosion.png')
iscollision_v= [False,False,False,False,False,False]


def explosion_fct(x,y):
    dis.blit(bumba_img,(x,y))
    global iscollision_v
    iscollision_v[i] = True


#big_boom
BOMBA_img = pygame.image.load('BOMBA.png')
BOMBAx = playerx
BOMBAy = playery
def BOMBA_fct(x,y):
    dis.blit(BOMBA_img,(x+16,y+10))
    global playery
    playery = 2000
damage = 0
#GAME LOOP
while  not running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10

            elif event.key == pygame.K_RIGHT:
                x_change = 10
            elif event.key == pygame.K_SPACE:
                if bullets == 'ready':
                    nr_bullets += 1
                    bulletx = playerx
                    bullet_foc(bulletx,bullety)
    dis.fill((34,54,9))
    pygame.display.update()

    full_life_fct()
    pygame.display.update()

    #MISCAREA
    for i in range(6):
            if alien_vectx[i] <= 0:
                alien_vectx[i] = 0
            elif alien_vectx[i] >= 768:
                alien_vectx[i] = 768
            if alien_vectx[i] == 768 or alien_vectx[i] == 0:
                xa_change[i] = -xa_change[i]
            alien_vectx[i] += xa_change[i]
            alien_fct(alien_vectx[i],alien_vecty[i])

    if bullety <= 0:
            bullety=playery
            bullets= 'ready'
    if bullets == 'fire':
        bullet_foc(bulletx,bullety)
        bullety-=15

    playerx += x_change
    player_fct(playerx,playery)
    pygame.display.update()
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    for i in range(6):
        if (bullety >= (alien_vecty[i] - 31) and bullety <= (alien_vecty[i] +31)) and (bulletx >= (alien_vectx[i] - 31) and bulletx <= (alien_vectx[i] +31)):
                explosion_fct(alien_vectx[i],alien_vecty[i])
                alien_vecty[i] = 1000
                bullety = 0
                score += 10
    #VERIFIC DACA TRECEM LA NIVELUL 2
    ok = 1
    for i in range(6):
        if iscollision_v[i] is False:
               ok = 0

    for i in range(6):
        if bullet_alien_status == 'ready':
            bullet_alien_fct(bullet_alien_vectx[i], bullet_alien_vecty[i])

    for i in range(6):
        if bullet_alien_vecty[i] >= 600:
            bullet_alien_vecty[i] = alien_vecty[i]
        if bullet_alien_status == 'fire':
            bullet_alien_fct(alien_vectx[i], bullet_alien_vecty[i])
            bullet_alien_vecty[i] += 2
        if (bullet_alien_vectx[i] >= (playerx - 63) and bullet_alien_vectx[i] <= (playerx + 63)) and (bullet_alien_vecty[i] >= (playery-63) and bullet_alien_vecty[i] <= (playery + 63)):
            explosion_player_fct(playerx,playery)
            bullet_alien_vecty[i] = alien_vecty[i]
            damage += 1
            a += 1
            score -= 5


    score_fct('score: ' +str(score))
    if damage == 20:
       for i in range(6):
            alien_vecty[i] = 2000
            bullet_alien_vecty[i] = 3000
       BOMBA_fct(playerx,playery)
       boss1y = 3000
       boss2y = 3000

       text2_fct(300,200)

    #LEVEL_2
    if ok == 1:

        boss1_fct(boss1x, boss1y)

        boss1x += bossx_change
        if boss1x <= 0:
            boss1x = 0
        elif boss1x >= 672:
            boss1x = 672
        if boss1x == 672 or boss1x == 0:
            bossx_change = (-1)*bossx_change
        boss1x += bossx_change
        bullet_boss1_fct(boss1x,bullet_boss1y )
        if bullet_boss1_status == 'ready':
            bullet_boss1_fct(bullet_boss1x,bullet_boss1y)
        if bullet_boss1y >= 600:
            bullet_boss1_status ='ready'
            bullet_boss1y = boss1y
        if bullet_boss1_status == 'fire':
            bullet_boss1y += 7

            bullet_boss1_fct(boss1x,bullet_boss1y)
        if distanta_boom_fct(bulletx,bullety,boss1x,boss1y) <= 80:
            bullety = 0
            DAMAGE1 += 1
            explosion_boss_fct(bulletx,boss1y)
        if distanta_boom_fct(bullet_boss1x,bullet_boss1y,playerx,playery) == 0:
            bullet_boss1y = boss1y
            explosion_player_fct(playerx,playery)
            score -= 10
            damage += 1
            a += 1



        #MOR MONSTRII
        if nr_inc == 0:
            if DAMAGE1 == 8:
                score += 50
                nr_inc += 1
                big_explosion_boss_fct(boss1x, boss1y)
                bullet_boss1x = 2000
                boss1y = 2000
                boss1x = 2000

        if boss1y == 2000:
            text_fct(200,300)
        #CAZ DACA AI PIERDUT LA NIVELUL 2
        if lost == 0:
            if damage == 20:
                for i in range(6):
                    alien_vecty[i] = 2000
                    bullet_alien_vecty[i] = 3000
                BOMBA_fct(playerx, playery)
                boss1y = 3000
                draw_life_fct(20)
                text2_fct(300, 200)
                lost += 1




    #statistici

    draw_life_fct(a)
    text3_fct(100,7)

    pygame.display.update()
    clock.tick(30)
    pygame.display.update()



pygame.quit()
quit()

    