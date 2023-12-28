import sys, pygame
pygame.init()

size = width, height = 920, 720
screen = pygame.display.set_mode(size)
black = 0, 0, 0
ball_speed = [3, 1]  # Adjust the initial speed as needed
ball_position = [width // 2, height // 2]
clock = pygame.time.Clock()

paddle2 = pygame.Rect(50, 5, 10, 80)
paddle2_prev_y = paddle2.y
paddle1 = pygame.Rect(width-50, 5, 10, 80)
paddle1_prev_y = paddle1.y

paddle_speed = 10

font = pygame.font.Font(None, 46)
cred_font = pygame.font.Font(None, 26)
text_color = (0, 100, 0)
score = 0
radius = 10
running = True  # Control variable for the game loop

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False  # Exit the loop and end the game

    # Allows user input to control paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle1.bottom < height:
        paddle1.y += paddle_speed
    if keys[pygame.K_w] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_s] and paddle2.bottom < height:
        paddle2.y += paddle_speed

    if keys[pygame.K_r]:
        # Reset the game state
        score = 0
        ball_position = [width // 2, height // 2]
        ball_speed = [5, 0]
        paddle1.y = (height - paddle1.height) // 2
        paddle2.y = (height - paddle2.height) // 2

    # Move the ball independently
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Ball collisions with walls
    if ball_position[0] < 0 or ball_position[0] > width:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] < 0 or ball_position[1] > height:
        ball_speed[1] = -ball_speed[1]

    # Ball collisions with paddles
    if paddle1.colliderect(pygame.Rect(ball_position[0]-10, ball_position[1]-10, 20, 20)) or \
       paddle2.colliderect(pygame.Rect(ball_position[0]-10, ball_position[1]-10, 20, 20)):
        score += 1
        ball_speed[0] = -ball_speed[0]  # Reverse the horizontal direction

        # Calculate the new vertical speed based on the position relative to the center of the paddle
        relative_position = (paddle1.centery - ball_position[1]) if ball_speed[0] > 0 else (paddle2.centery - ball_position[1])
        ball_speed[1] = relative_position / 100  # Experiment with the scaling factor

    # Check if the game is over
    if ball_position[0] <= 0 or ball_position[0] >= width and score > 1:
        game_over_text = font.render("Game Over! Press R to restart", True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(game_over_text, game_over_text_rect)
        pygame.display.flip()  # Ensure the "Game Over!" text is displayed

        restart_pressed = False
        while not restart_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Exit the loop and end the game
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    restart_pressed = True

    paddle1_prev_y = paddle1.y
    paddle2_prev_y = paddle2.y

    screen.fill(black)
    pygame.draw.rect(screen, (215, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)

    # Draw the ball
    pygame.draw.circle(screen, (200, 200, 200), (int(ball_position[0]), int(ball_position[1])), radius)
    pygame.draw.line(screen, (255, 255, 255), ((width / 2), 0), ((width / 2), height))

    # Render text
    text = font.render("Score: " + str(score), True, text_color)
    text_rect = text.get_rect(center=(width // 2, 25))
    screen.blit(text, text_rect)

    cred = cred_font.render("Developed by Josiah Mbao", True, text_color)
    cred_text_rect = cred.get_rect(center=(width - 120, height - 15))
    screen.blit(cred, cred_text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
