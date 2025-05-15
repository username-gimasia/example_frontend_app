import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 400
BLOCK  = 20
FPS    = 10

# Цвета
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)

# Настройка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock  = pygame.time.Clock()
pygame.display.set_caption("Snake Game")

# Функция рисования змейки
def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK, BLOCK))

# Основной игровой цикл
def game_loop():
    # Начальные параметры змейки
    x = WIDTH // 2
    y = HEIGHT // 2
    dx, dy = 0, 0
    snake = [[x, y]]
    snake_length = 1

    # Случайная еда
    food_x = random.randrange(0, WIDTH, BLOCK)
    food_y = random.randrange(0, HEIGHT, BLOCK)

    score = 0
    font = pygame.font.SysFont(None, 36)

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK, 0

        # Движение змейки
        x += dx
        y += dy

        # Проверка границ
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            break  # Игра окончена

        # Расширяем тело
        snake.insert(0, [x, y])
        if len(snake) > snake_length:
            snake.pop()

        # Проверка столкновения с собой
        if [x, y] in snake[1:]:
            break  # Игра окончена

        # Съедание еды
        if x == food_x and y == food_y:
            score += 1
            snake_length += 1
            food_x = random.randrange(0, WIDTH, BLOCK)
            food_y = random.randrange(0, HEIGHT, BLOCK)

        # Отрисовка
        screen.fill(BLACK)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, BLOCK, BLOCK))

        # Вывод счета
        score_surf = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Игра окончена — вывод финального счета
    msg = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
