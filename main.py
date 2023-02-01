from ipaddress import collapse_addresses
import pygame
from Chess_Game.constants import *

pygame.init()
Clock = pygame.time.Clock()

Window = pygame.display.set_mode((Width, Height))

def get_position(x, y):
    row = y//Square
    col = x//Square


def main():
    run = True
    FPS = 60
    while run:
        Clock.tick(FPS)
        Window.blit(White_Bishop, (50, 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE and Game_Over:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN and not Game_Over:
                if pygame.mouse.get_pressed()[0]:
                    location = pygame.mouse.get_pos()
                    row, col = get_position(location[0], location[1])


main()
