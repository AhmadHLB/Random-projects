import pygame
import os

from pygame import key

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255, 255, 255)
SPEED = 5
BULLET_SPEED = 5

FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 50

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
SPACE_IMAGE = pygame.image.load(os.path.join('Assets', 'space.png'))


YELLOW_SPACESHIP =pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), (90))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), (-90))
SPACE = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))

def draw_window(yellow, red):
        WIN.fill(WHITE)
        WIN.blit(SPACE_IMAGE, (0, 0))
        WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
        WIN.blit(RED_SPACESHIP, (red.x, red.y))

def shoot(color, bullets):
    BULLET = pygame.draw.rect(color.x, color.y, 10, 10)
    bullets.append(BULLET)


def main():
    yellow = pygame.Rect(200, 225, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(650, 225, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    bullets_red = []
    bullets_yellow = []

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:
            red.y -= SPEED
        if keys_pressed[pygame.K_DOWN]:
            red.y += SPEED
        if keys_pressed[pygame.K_LEFT]:
            red.x -= SPEED
        if keys_pressed[pygame.K_RIGHT]:
            red.x += SPEED

        if keys_pressed[pygame.K_w]:
            yellow.y -= SPEED
        if keys_pressed[pygame.K_s]:
            yellow.y += SPEED
        if keys_pressed[pygame.K_a]:
            yellow.x -= SPEED
        if keys_pressed[pygame.K_d]:
            yellow.x += SPEED

        if keys_pressed[pygame.K_SPACE]:
            shoot(yellow, bullets_yellow)

        draw_window(yellow, red)

        for bullet in bullets_yellow:
            bullet.x += BULLET_SPEED

        pygame.display.update()

    pygame.quit()

if __name__ == '_main_':
    main()