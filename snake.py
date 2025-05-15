import pygame

BLOCK_SIZE = 20
SNAKE_COLOR = (0, 200, 0)

class Snake:
    def __init__(self, start_pos):
        self.blocks = [start_pos]       # список координат блоков
        self.direction = (BLOCK_SIZE, 0)  # изначально едет вправо
        self.grow_next = False

    def set_direction(self, new_dir):
        # Запрещаем разворот на 180°
        if (new_dir[0] == -self.direction[0] and
            new_dir[1] == -self.direction[1]):
            return
        self.direction = new_dir

    def move(self):
        head_x, head_y = self.blocks[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        self.blocks.insert(0, new_head)
        if self.grow_next:
            self.grow_next = False
        else:
            self.blocks.pop()  # убираем хвост

    def grow(self):
        self.grow_next = True

    def draw(self, surface):
        for x, y in self.blocks:
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, SNAKE_COLOR, rect)

    def collides_with_self(self):
        return self.blocks[0] in self.blocks[1:]

    def get_head_pos(self):
        return self.blocks[0]
