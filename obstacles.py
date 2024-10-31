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

