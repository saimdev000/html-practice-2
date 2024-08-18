import pygame 
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Ball")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up player
player_width, player_height = 100, 20
player_x = (width - player_width) // 2
player_y = height - player_height - 10
player_speed = 5

# Set up ball
ball_size = 20
ball_x = random.randint(0, width - ball_size)
ball_y = 0
ball_speed = 5

# Game variables
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed
    
    # Move ball
    ball_y += ball_speed
    if ball_y > height:
        ball_x = random.randint(0, width - ball_size)
        ball_y = 0

    # Check for collision
    if (player_x < ball_x + ball_size and
        player_x + player_width > ball_x and
        player_y < ball_y + ball_size and
        player_y + player_height > ball_y):
        score += 1
        ball_x = random.randint(0, width - ball_size)
        ball_y = 0

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, black, (player_x, player_y, player_width, player_height))
    pygame.draw.ellipse(screen, red, (ball_x, ball_y, ball_size, ball_size))

    # Display score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
