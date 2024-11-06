# Snake Game

A classic Snake Game built with Python and Pygame, featuring colorful backgrounds, dynamic obstacles, and increasing difficulty as the snake grows.

## Table of Contents
- [Features](#features)
- [Game Rules](#game-rules)
- [Installation](#installation)
- [How to Play](#how-to-play)


---

## Features
- **Dynamic Backgrounds**: The background color changes each time the snake eats food.
- **Randomized Obstacles**: Red obstacles are placed on the screen for the snake to avoid.
- **Gradient Background Effect**: A gradient effect enhances the game’s visual appeal.
- **Growing Snake**: The snake increases in length and speed each time it eats food.
- **Game Over Screen**: Clear options to restart or quit when the game is over.

## Game Rules
1. Control the snake to eat the food that appears randomly on the screen.
2. Avoid hitting the screen boundaries or obstacles.
3. The game ends if the snake hits the boundaries, an obstacle, or itself.

## Installation
1. Ensure Python is installed on your machine (Python 3.6+ recommended).
2. Install Pygame:
   ```bash
   pip install pygame
### Cloning the Project

To clone this project, follow these steps:

1. Open your terminal.
2. Navigate to the desired directory where you want to clone the project.
3. Use the following command to clone the repository:

   ```bash
   git clone https://github.com/temora3/SnakeGame.git

## How to Play

1. **Start the Game**:
   - Run the game using the command:
     ```bash
     python snake_game.py
     ```
   - The game window will open with a colorful gradient background and a black snake in the center.

2. **Game Controls**:
   - Use the **Arrow Keys** on your keyboard to control the snake's movement:
     - **Up Arrow**: Move up
     - **Down Arrow**: Move down
     - **Left Arrow**: Move left
     - **Right Arrow**: Move right
   - Note: The snake cannot reverse direction (e.g., if you’re moving left, pressing the right arrow won’t reverse it).

3. **Objective**:
   - Guide the snake to eat the **white food circle** that appears randomly on the screen.
   - Each time the snake eats the food:
     - It grows in length.
     - The background changes color.
     - The game’s speed increases, making it more challenging.

4. **Avoid Obstacles**:
   - Red obstacles are scattered around the screen; avoid them to prevent game over.
   - Avoid running into the screen boundaries or the snake's own body.

5. **Game Over**:
   - The game will end if:
     - The snake collides with an obstacle, the boundary, or itself.
   - When the game is over, a message appears with the options:
     - **Press `C`** to play again from the beginning.
     - **Press `Q`** to quit the game.

6. **Winning Strategy**:
   - Be cautious of your growing snake’s length and speed as the game progresses.
   - Plan your moves in advance to avoid collisions with obstacles or the snake’s own body.

Enjoy the challenge, and see how long you can grow your snake!
