import sys, pygame
from modules.snake import Snake, BLOCK_SIZE
from modules.food  import Food

# Параметры окна
WIDTH, HEIGHT = 600, 400
FPS = 10
BG_COLOR = (0,0,0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Модульная Змейка 🐍")
    clock = pygame.time.Clock()

    snake = Snake(start_pos=(WIDTH//2, HEIGHT//2))
    food  = Food(screen_width=WIDTH, screen_height=HEIGHT)
    score = 0
    font  = pygame.font.SysFont(None, 30)

    running = True
    while running:
        # 1) События
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    snake.set_direction((0, -BLOCK_SIZE))
                elif e.key == pygame.K_DOWN:
                    snake.set_direction((0, BLOCK_SIZE))
                elif e.key == pygame.K_LEFT:
                    snake.set_direction((-BLOCK_SIZE, 0))
                elif e.key == pygame.K_RIGHT:
                    snake.set_direction((BLOCK_SIZE, 0))

        # 2) Логика
        snake.move()
        head = snake.get_head_pos()

        # Проверка границ
        if not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT):
            break

        # Съели еду?
        if head == food.position:
            score += 1
            snake.grow()
            food.randomize()

        # Само­столкновение
        if snake.collides_with_self():
            break

        # 3) Отрисовка
        screen.fill(BG_COLOR)
        snake.draw(screen)
        food.draw(screen)
        score_surf = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_surf, (10,10))

        pygame.display.flip()
        clock.tick(FPS)

    # Game Over
    msg = font.render(f"Game Over! Score: {score}", True, (255,50,50))
    screen.blit(
        msg,
        (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2)
    )
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
