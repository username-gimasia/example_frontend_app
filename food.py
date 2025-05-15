import pygame, random
from modules.snake import BLOCK_SIZE

FOOD_COLOR = (200, 0, 0)

class Food:
    def __init__(self, screen_width, screen_height):
        self.area_w = screen_width
        self.area_h = screen_height
        self.position = (0, 0)
        self.randomize()

    def randomize(self):
        cols = self.area_w // BLOCK_SIZE
        rows = self.area_h // BLOCK_SIZE
        self.position = (
            random.randrange(0, cols) * BLOCK_SIZE,
            random.randrange(0, rows) * BLOCK_SIZE
        )

    def draw(self, surface):
        x, y = self.position
        rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(surface, FOOD_COLOR, rect)
