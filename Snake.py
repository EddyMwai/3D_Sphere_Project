import json
import os

import pygame
import random

pygame.init()
pygame.mixer.init()

# Load background music
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)

# Load sound effects
eat_sound = pygame.mixer.Sound('eat_food.mp3')
hit_sound = pygame.mixer.Sound('impact.mp3')
game_over_sound = pygame.mixer.Sound('game_over_sound.mp3')

background_colors = [
    (0, 0, 255),  # 0: Blue
    (252, 114, 114),  # 1: Red
    (205, 255, 169),  # 2: Green
    (255, 165, 0),  # 3: Orange
    (128, 0, 128),  # 4: Purple
    (255, 255, 0),  # 5: Yellow
    (253, 173, 206),  # 6: Pink
    (255, 255, 224)  # 7: Cream
]

white = (255, 255, 255)
black = (0, 0, 0)
highlight_color = (100, 100, 255)  # HighlightS color for selected option

width, height = 600, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Enhanced Snake Game')

snake_block = 20
initial_speed = 5
snake_speed = initial_speed
lives = 5

# Load assets
heart_image = pygame.image.load('heart.png')  # Add a heart image (20x20 px) in the working directory
heart_outline = pygame.image.load('heart-outline.png')  # Heart outline for missing lives
food_image = pygame.image.load('food.png')  # Add an apple image (20x20 px) in the working directory

clock = pygame.time.Clock()

font_style = pygame.font.Font(pygame.font.match_font('arial'), 15)

high_scores_file = "high_scores.json"

HUD_HEIGHT = 50  # Height of the HUD area at the top of the screen that has the lives and highscore

score = 0
difficulty = ""
player_name = ""


def draw_menu(selected_index, options):
    display.fill(black)
    for index, option in enumerate(options):
        color = highlight_color if index == selected_index else white
        text_surface = font_style.render(option, True, color)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2 - 50 + index * 50))
        display.blit(text_surface, text_rect)
    pygame.display.update()


def draw_hud(lives, score):
    pygame.draw.rect(display, white, (0, 0, width, HUD_HEIGHT))  # Background for HUD
    draw_lives(lives)
    draw_score(score)


def difficulty_menu():
    options = ["Easy", "Medium", "Hard", "Adaptive"]
    selected_index = 0
    menu_active = True

    while menu_active:
        draw_menu(selected_index, options)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Move up
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:  # Move down
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:  # Select option
                    return options[selected_index].lower()


def draw_game_over_menu(selected_index, options, title=None):
    display.fill(black)
    if title:
        title_surface = font_style.render(title, True, white)
        title_rect = title_surface.get_rect(center=(width // 2, height // 4))
        display.blit(title_surface, title_rect)

    for index, option in enumerate(options):
        color = highlight_color if index == selected_index else white
        text_surface = font_style.render(option, True, color)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2 + index * 50))
        display.blit(text_surface, text_rect)

    pygame.display.update()


def load_high_scores():
    if os.path.exists(high_scores_file):
        try:
            with open(high_scores_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("High scores file is empty or invalid. Resetting high scores.")
            return {"easy": [], "medium": [], "hard": [], "adaptive": []}
    else:
        return {"easy": [], "medium": [], "hard": [], "adaptive": []}


def save_high_scores(high_scores):
    with open(high_scores_file, 'w') as file:
        json.dump(high_scores, file)


def draw_score(score):
    score_text = font_style.render(f"Score: {score}", True, black)
    display.blit(score_text, (width - 120, 10))  # Top-right corner


def input_name_screen():
    name = ""
    active = True

    while active:
        display.fill(black)
        prompt = font_style.render("Enter your name: ", True, white)
        name_surface = font_style.render(name, True, highlight_color)
        display.blit(prompt, (50, 250))
        display.blit(name_surface, (50, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode


def game_over_menu(score, difficulty, player_name):
    options = ["Play Again", "Quit"]
    selected_index = 0
    menu_active = True

    # Load existing high scores
    high_scores = load_high_scores()

    # Ensure there's an entry for the current difficulty
    if difficulty not in high_scores:
        high_scores[difficulty] = []

    high_scores[difficulty].append({"name": player_name, "score": score})

    valid_scores = []
    for entry in high_scores[difficulty]:
        try:
            # Convert score to integer;
            entry["score"] = int(entry["score"])
            valid_scores.append(entry)
        except (ValueError, TypeError):
            print(f"Invalid score entry skipped: {entry}")

    # Sort and keep only the top 5 scores
    high_scores[difficulty] = sorted(
        valid_scores, key=lambda x: x["score"], reverse=True
    )[:5]

    save_high_scores(high_scores)

    while menu_active:
        display.fill(black)
        title = f"Game Over - Score: {score}"
        title_surface = font_style.render(title, True, white)
        title_rect = title_surface.get_rect(center=(width // 2, height // 6))
        display.blit(title_surface, title_rect)

        high_score_title = font_style.render(f"High Scores ({difficulty.capitalize()}):", True, white)
        display.blit(high_score_title, (50, 200))
        for i, entry in enumerate(high_scores[difficulty]):
            entry_text = f"{i + 1}. {entry['name']} - {entry['score']}"
            entry_surface = font_style.render(entry_text, True, white)
            display.blit(entry_surface, (50, 250 + i * 30))

        for index, option in enumerate(options):
            color = highlight_color if index == selected_index else white
            text_surface = font_style.render(option, True, color)
            text_rect = text_surface.get_rect(center=(width // 2, height // 2 + index * 50))
            display.blit(text_surface, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:
                        return "play"
                    elif selected_index == 1:
                        return "quit"


def draw_gradient(color1, color2):
    for i in range(height):
        color = [
            color1[j] + (color2[j] - color1[j]) * i // height for j in range(3)
        ]
        pygame.draw.line(display, color, (0, i), (width, i))


def input_name_screen():
    name = ""
    active = True

    while active:
        display.fill(black)
        prompt = font_style.render("Enter your name: ", True, white)
        name_surface = font_style.render(name, True, highlight_color)
        display.blit(prompt, (50, 250))
        display.blit(name_surface, (50, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode


def our_snake(snake_list):
    for i, x in enumerate(snake_list):
        gradient_color = (0, 255 - (i * 10), 0)
        pygame.draw.rect(display, gradient_color, (x[0], x[1], snake_block, snake_block), border_radius=8)
        shadow_color = (0, 100, 0)
        pygame.draw.rect(display, shadow_color, (x[0] + 2, x[1] + 2, snake_block, snake_block), border_radius=8)


def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(display, (139, 69, 19), obstacle)


def draw_lives(lives):
    spacing = 30
    start_x = 10
    start_y = 10
    for i in range(5):
        if i < lives:
            display.blit(heart_image, (start_x + i * spacing, start_y))
        else:
            display.blit(heart_outline, (start_x + i * spacing, start_y))


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])


def game_loop():
    global snake_speed, lives
    global score
    score = 0
    game_over = False
    game_close = False

    player_name = input_name_screen()

    difficulty = difficulty_menu()
    if difficulty == "easy":
        snake_speed = 5
    elif difficulty == "medium":
        snake_speed = 7
    elif difficulty == "hard":
        snake_speed = 15
    elif difficulty == "adaptive":
        snake_speed = 5

    lives = 5

    x1 = width / 2
    y1 = HUD_HEIGHT + height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = random.randint(0, (width - snake_block) // snake_block) * snake_block
    foody = random.randint(HUD_HEIGHT // snake_block, (height - snake_block) // snake_block) * snake_block
    current_color_index = 0

    obstacles = [
        pygame.Rect(100, 100, snake_block * 3, snake_block),
        pygame.Rect(400, 300, snake_block, snake_block * 3),
        pygame.Rect(250, 450, snake_block * 2, snake_block),
    ]

    paused = False

    while not game_over:
        while game_close:
            pygame.mixer.music.stop()
            game_over_sound.play()
            result = game_over_menu(score, difficulty, player_name)
            if result == "play":
                pygame.mixer.music.load('background_music.mp3')
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1, 0.0)
                game_loop()
            elif result == "quit":
                pygame.quit()
                quit()

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
                if paused:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                        paused = False
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                        paused = False
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                        paused = False
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
                        paused = False
                else:
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

        if not paused:
            if x1 >= width or x1 < 0 or y1 >= height or y1 < HUD_HEIGHT:
                lives -= 1
                if lives == 0:
                    game_close = True
                x1, y1 = width / 2, height / 2
                x1_change, y1_change = 0, 0
                paused = True

            x1 += x1_change
            y1 += y1_change

            color1 = background_colors[current_color_index % len(background_colors)]
            color2 = (color1[0] // 2, color1[1] // 2, color1[2] // 2)
            draw_gradient(color1, color2)

            display.blit(food_image, (foodx, foody))
            draw_obstacles(obstacles)
            draw_lives(lives)
            draw_score(score)
            draw_hud(lives, score)

            snake_head_rect = pygame.Rect(x1, y1, snake_block, snake_block)
            for obstacle in obstacles:
                if snake_head_rect.colliderect(obstacle):
                    hit_sound.play()
                    lives -= 1
                    if lives == 0:
                        game_close = True
                    x1, y1 = width / 2, height / 2
                    x1_change, y1_change = 0, 0
                    paused = True

            snake_Head = [x1, y1]
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    lives -= 1
                    if lives == 0:
                        game_close = True
                    x1, y1 = width / 2, height / 2
                    x1_change, y1_change = 0, 0
                    paused = True

            our_snake(snake_List)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                eat_sound.play()
                foodx = random.randint(0, (width - snake_block) // snake_block) * snake_block
                foody = random.randint(HUD_HEIGHT // snake_block, (height - snake_block) // snake_block) * snake_block
                Length_of_snake += 1
                score += 1
                if difficulty == "adaptive":
                    snake_speed += 0.5
                current_color_index += 1

            clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()