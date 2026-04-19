🐍 Snake Game with Persistent High Score
A classic Snake game built using Python's Turtle Graphics module. This project demonstrates advanced Object-Oriented Programming (OOP) principles, including class inheritance, encapsulation, and local file manipulation for persistent data storage.

🌟 Key Features
Persistent High Score: Uses Python's file I/O system to store and retrieve your best score from a data.txt file, ensuring your progress is saved even after closing the game.

Object-Oriented Design: The game is organized into specialized classes (Snake, Food, Scoreboard, and GameMech) to ensure clean, maintainable, and modular code.

Direction Lock Logic: Includes custom logic to prevent "illegal turns" (180-degree snaps), which prevents the snake from accidentally colliding with itself during rapid key presses.

Interactive Menus: Features an in-game UI that allows players to choose between restarting or exiting upon death.

Dynamic Difficulty: The snake's speed increases by 5% every time it eats food, making the game progressively more challenging.

🛠️ Project Structure
The project is split into several modules to follow the Single Responsibility Principle:

main.py: The entry point of the application that initializes and runs the game loop.

game_mechanics.py: The "Brain" of the project; coordinates interactions between the snake, food, and scoreboard.

snake.py: Manages the snake's body segments, movement, and growth logic.

food.py: Handles the random spawning of food items on the screen.

scoreboard.py: Manages the UI, score tracking, and file I/O for the high score.

data.txt: A plain text file used to store the high score integer.

🚀 Getting Started
Prerequisites
Python 3.x

No external libraries required (uses the built-in turtle, time, and random modules).

Installation
Clone the repository:

Bash

git clone https://github.com/your-username/snake-game-highscore.git
cd snake-game-highscore
Ensure data.txt exists: Create a file named data.txt in the root directory and type 0 inside it.

Run the game:

Bash

python main.py
🎮 How to Play
Up Arrow: Move Up

Down Arrow: Move Down

Left Arrow: Move Left

Right Arrow: Move Right

Objective: Eat the blue food to grow and increase your score.

Game Over: The game ends if you hit the wall or your own tail.