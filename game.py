import pygame
import random
import time
import sys
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Dodge')
BG = pygame.transform.scale(pygame.image.load('space.jpeg'), (WIDTH, HEIGHT))

PLR_W, PLR_H = 40, 60
VEL = 5
FPS = 60
STAR_W, STAR_H = 10, 20
FONT = pygame.font.SysFont('impact',30)
hit = False

stars = []

def draw(player, timePassed, stars):
    WIN.blit(BG, (0, 0))
    timeText = FONT.render(f"Time: {round(timePassed)}s", 1, 'white')
    WIN.blit(timeText, (10, 10))
    pygame.draw.rect(WIN, (255, 0, 0), player)
    for star in stars:
        pygame.draw.rect(WIN, 'orange', star)
    pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()

def main():
    run = True
    starCount = 0
    starAddIncrement = 3000
    maxStars = 3

    while run:
        starCount += clock.tick(FPS)
        elapsedTime = time.time() - startTime

        if starCount > starAddIncrement:
            for _ in range(random.randint(1, maxStars)):
                starX = random.randint(0, WIDTH - STAR_W)
                star = pygame.Rect(starX, -STAR_H, STAR_W, STAR_H)
                stars.append(star)

            starAddIncrement = max(200, starAddIncrement-50)
            starCount = 0
            maxStars += random.randint(1, 2)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                terminate()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            terminate()
        if keys[pygame.K_LEFT] and player.x - VEL >= 0:
            player.x -= VEL
        if keys[pygame.K_RIGHT] and player.x + VEL + player.width <= 1000:
            player.x += VEL

        for s in stars[:]:
            s.y += VEL
            if s.y > HEIGHT:
                stars.remove(s)
            elif s.y+s.height >= player.y and s.colliderect(player):
                stars.remove(s)
                hit = True
                terminate()
        draw(player, elapsedTime, stars)

player = pygame.Rect(200, HEIGHT-PLR_H, PLR_W, PLR_H)
clock = pygame.time.Clock()
startTime = time.time()
elapsedTime = 0

if __name__ == '__main__':
    main()
