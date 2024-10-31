import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
background_colors = [
    (0, 0, 255),    # 0: Blue
    (255, 0, 0),    # 1: Red
    (0, 255, 0),    # 2: Green
    (255, 165, 0),  # 3: Orange
    (128, 0, 128),  # 4: Purple
    (255, 255, 0),  # 5: Yellow
    (139, 69, 19),  # 6: Brown
    (255, 192, 203),# 7: Pink
    (255, 255, 224) # 8: Cream
]

# Set up display
width, height = 600, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Game parameters
snake_block = 20
initial_speed = 5  # Start speed
snake_speed = initial_speed

# Set up the clock
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)

def draw_gradient(color1, color2):
    for i in range(height):
        color = [
            color1[j] + (color2[j] - color1[j]) * i // height for j in range(3)
        ]
        pygame.draw.line(display, color, (0, i), (width, i))

def draw_sphere(x, y, radius):
    pygame.draw.circle(display, (255, 255, 255), (x, y), radius)  # White food

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(display, (0, 0, 0), (x[0] + snake_block // 2, x[1] + snake_block // 2), snake_block // 2)  # Black snake

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(display, (255, 0, 0), obstacle)  # Red obstacles

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

def game_loop():
    global snake_speed  # Use the global variable for speed
    game_over = False
    game_close = False

    snake_speed = initial_speed  # Reset speed to initial speed

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = random.randint(0, (width - snake_block) // snake_block) * snake_block
    foody = random.randint(0, (height - snake_block) // snake_block) * snake_block

    current_color_index = 0  # Start with the first background color

    # Define obstacle positions and dimensions
    obstacles = [
        pygame.Rect(100, 100, snake_block * 3, snake_block),   # Horizontal wall
        pygame.Rect(400, 300, snake_block, snake_block * 3),   # Vertical wall
        pygame.Rect(250, 450, snake_block * 2, snake_block),
        pygame.Rect(450, 100, snake_block * 2, snake_block),
        pygame.Rect(150, 200, snake_block, snake_block * 4),
        pygame.Rect(300, 200, snake_block, snake_block * 4),
        pygame.Rect(300, 100, snake_block * 2, snake_block),
        pygame.Rect(150, 400, snake_block, snake_block * 4),
        pygame.Rect(350, 150, snake_block, snake_block * 4),
        # Another horizontal wall
    ]

    while not game_over:

        while game_close:
            display.fill((0, 0, 0))  # Black background for game over
            message("You Lost! Press C to play again or Q to Quit", (255, 0, 255))  # Red message
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if snake collides with the wall boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        # Draw the gradient background
        color1 = background_colors[current_color_index % len(background_colors)]
        color2 = (color1[0] // 2, color1[1] // 2, color1[2] // 2)  # Darker version for gradient
        draw_gradient(color1, color2)

        draw_sphere(foodx + snake_block // 2, foody + snake_block // 2, snake_block // 2)

        # Draw obstacles and check for collision with the snake's head
        draw_obstacles(obstacles)
        snake_head_rect = pygame.Rect(x1, y1, snake_block, snake_block)
        for obstacle in obstacles:
            if snake_head_rect.colliderect(obstacle):
                game_close = True

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        # Check if snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = random.randint(0, (width - snake_block) // snake_block) * snake_block
            foody = random.randint(0, (height - snake_block) // snake_block) * snake_block
            Length_of_snake += 1
            snake_speed += 0.5  # Increase speed by 2
            current_color_index += 1  # Change background color

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
game_loop()