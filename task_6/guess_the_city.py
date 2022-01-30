import os
import random

import pygame

from show_img import show_img

ALL_CITIES = [
    'Москва',
    'Нью-Йорк',
    'Лондон',
    'Токио',
    'Стамбул',
    'Каир',
    'Буэнос-Айрес',
    'Париж',
    'Дубай'
    'Мюнхен'
]


def main():
    index = random.randrange(0, len(ALL_CITIES))
    map_file = show_img(ALL_CITIES[index])
    pygame.init()
    pygame.display.set_caption('Угадай-ка город')
    screen = pygame.display.set_mode((600, 450))
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                index = random.randrange(0, len(ALL_CITIES))
                map_file = show_img(ALL_CITIES[index])

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)


if __name__ == '__main__':
    main()
