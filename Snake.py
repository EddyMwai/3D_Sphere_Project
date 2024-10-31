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

