import sys, pygame
pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
black = 0, 0, 0
ball_speed = [5, 0]  # Adjust the initial speed as needed
ball_position = [width // 2, height // 2]
clock = pygame.time.Clock()

paddle2 = pygame.Rect(50, 5, 10, 80)
paddle2_prev_y = paddle2.y 
paddle1 = pygame.Rect(width-50, 5, 10, 80)
paddle1_prev_y = paddle1.y 

paddle_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

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
        ball_speed[1] += (paddle1.y - paddle1_prev_y) / 25  # Experiment with the scaling factor
        ball_speed[1] += (paddle2.y - paddle2_prev_y) / 25
        ball_speed[0] = -ball_speed[0]

    paddle1_prev_y = paddle1.y
    paddle2_prev_y = paddle2.y

    screen.fill(black)
    pygame.draw.rect(screen, (215, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)

    # Draw the ball
    pygame.draw.circle(screen, (200, 200, 200), (int(ball_position[0]), int(ball_position[1])), 10)
    
    pygame.display.flip()
    clock.tick(60)