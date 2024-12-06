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
- **Randomized Obstacles**: Red obstacles are placed randomly on the screen for the snake to avoid.
- **Gradient Background Effect**: A visually appealing gradient effect enhances the gameplay experience.
- **Growing Snake**: The snake grows in length and speed with each piece of food it eats.
- **Game Over Screen**: Includes clear options to restart or quit.

---

## Game Rules
1. Control the snake to eat the food that appears randomly on the screen.
2. Avoid colliding with the screen boundaries, obstacles, or the snake's own body.
3. The game ends if the snake hits the boundaries, an obstacle, or itself.

---

## Installation

### Step 1: Install Python
1. Check if Python is installed:
   - Open your terminal (Command Prompt on Windows or Terminal on macOS/Linux).
   - Type: `python --version`
   - If a version number is displayed, Python is already installed.
2. Download Python (if not installed):
   - Visit [python.org/downloads](https://www.python.org/downloads/).
   - Download and install the latest version of Python for your system.
   - During installation, ensure you check the box that says "Add Python to PATH."

### Step 2: Install Pygame
1. Open your terminal or command prompt.
2. Run the following command to install Pygame:
   
    `pip install pygame`

### Step 3: Clone the Project
1. Open your terminal.
2. Navigate to the directory where you'd like to store the project.
3. Clone the repository using the command:

   `git clone https://github.com/temora3/SnakeGame.git`

---

## How to Play

1. **Start the Game**:
   - Run the game with the command:

      `python snake_game.py`
   - A game window will open, featuring a colorful gradient background and a black snake in the center.

2. **Game Controls**:
   - Use the **arrow keys** on your keyboard to move the snake:
     - **Up Arrow**: Move up
     - **Down Arrow**: Move down
     - **Left Arrow**: Move left
     - **Right Arrow**: Move right
   - Note: The snake cannot reverse direction (e.g., pressing the right arrow while moving left won't work).

3. **Objective**:
   - Guide the snake to eat the **white food circle** that appears randomly on the screen.
   - Each time the snake eats food:
     - It grows longer.
     - The background color changes.
     - The game speed increases, making it more challenging.

4. **Avoid Obstacles**:
   - Red obstacles are scattered randomly on the screen; avoid them.
   - Avoid colliding with the screen boundaries or the snake's own body.

5. **Game Over**:
   - The game ends if:
     - The snake hits an obstacle, the screen boundary, or itself.
   - After the game ends, a message appears with two options:
     - **Press `C`** to restart the game.
     - **Press `Q`** to quit.

6. **Winning Strategy**:
   - Be mindful of your growing snake’s length and speed as the game progresses.
   - Plan your movements in advance to avoid collisions.

---

Enjoy the game, and challenge yourself to grow the longest snake possible! 🚀
