import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")


PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15


player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)


ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

player_score = 0
ai_score = 0
font = pygame.font.Font(None, 74)


running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= 10
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 10

    
    if ai_paddle.centery < ball.centery and ai_paddle.bottom < HEIGHT:
        ai_paddle.y += 5
    if ai_paddle.centery > ball.centery and ai_paddle.top > 0:
        ai_paddle.y -= 5

    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_speed_x *= -1

    
    if ball.left <= 0:
        ai_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    elif ball.right >= WIDTH:
        player_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, ai_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    
    player_text = font.render(str(player_score), True, WHITE)
    ai_text = font.render(str(ai_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(ai_text, (WIDTH * 3 // 4, 20))

    pygame.display.flip()


pygame.quit()
