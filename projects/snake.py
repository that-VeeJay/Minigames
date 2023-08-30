import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake and food
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (width//10)) * 10,
                 random.randrange(1, (height//10)) * 10]
food_spawn = True

# Directions
direction = 'RIGHT'
change_to = direction

# Score
score = 0

# Speed
speed = 15

# Game Over
game_over = False

# Score font
font = pygame.font.Font(None, 36)

# Main Function
def gameLoop():
    global direction
    global change_to
    global snake_position
    global food_position
    global food_spawn
    global score
    global game_over

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Validation of direction
        if change_to == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = [random.randrange(1, (width//10)) * 10,
                             random.randrange(1, (height//10)) * 10]
        food_spawn = True

        # Draw the snake and food
        display.fill(black)
        for pos in snake_body:
            pygame.draw.rect(display, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(display, white,
                         pygame.Rect(food_position[0], food_position[1], 10, 10))

        # Draw the score
        score_text = font.render(f"Score: {score}", True, white)
        display.blit(score_text, (10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > width-10:
            game_over = True
        if snake_position[1] < 0 or snake_position[1] > height-10:
            game_over = True

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over = True

        pygame.display.update()
        pygame.time.Clock().tick(speed)

    pygame.quit()
    quit()

# Calling the main function
gameLoop()

# August31 edit
# I have edited this file.

# This is the changes for the Fixtemp

# testbranch changes