Base PacMan game taken from https://github.com/x4nth055/pythoncode-tutorials.git

Authored By: Camon Buller, Exequiel Rodriguez Barri, and Alexander Stockton

# AI Concepts Implemented

Stochastic Movement: The ghosts have a 60% every move to change directions. If the space next to them in the new direction is a wall, they'll continue in the direction they were already going. If the next space in front of them is a wall, they will choose a new direction.
Automated Pathfinding: PACMAN switches between BFS, DFS, A*, and UCS search algorithms when searching the state space (static maze) for score balls. He also tries his best to avoid ghosts.

# Algorithm Choices and Justification

We implemented `Breadth First`, `Depth-First`, `A*`, and `Uniform Cost` searches into the player AI. This allows the player to see how each algorithm chooses paths differently. Each path seeks the score balls instead of avoiding ghosts.

# Challenges Faced and Solutions

Needed a way to toggle PACMAN's AI to shift between search algorithms. Accomplished this by a comparison of strings on the ALGORITHM variable in options.py. Pressing the key 1, 2, 3, or 4 will switch between BFS, DFS, A*, and UCS respectively. Press T to toggle AI OFF/ON, arrow-keys to move w/out AI

# Code Documentation

*Documentation compiled by Gemini 2.5 Pro on December 1, 2025.*

This document provides an overview of the project's Python files and their roles.

## Core Gameplay & Logic

This section covers the main entry point, game world management, and configuration.

* **`main.py`**: This is the main entry point for the game. It initializes Pygame, sets up the display window, and runs the main game loop. It creates an instance of the `World` class to manage the game state.
* **`world.py`**: This file is the heart of the game's logic. It manages the game world, including generating levels from the `MAP` constant, handling game state transitions (like advancing to a new level or game over), and updating all game entities (Pac-Man, ghosts, berries). It also contains the main `update` loop that drives the game.
* **`settings.py`**: This file centralizes all the game's constants and settings. It defines the `MAP` layout, screen dimensions (`WIDTH`, `HEIGHT`), character speeds (`PLAYER_SPEED`, `GHOST_SPEED`), the default pathfinding `ALGORITHM`, and other configurable parameters.

## Character & Entities

This section describes the classes for the player, enemies, and other interactive objects.

* **`pac.py`**: Defines the `Pac` class for the player character. This class handles Pac-Man's movement (both manual and AI-controlled), animation, scoring, and lives. It integrates the pathfinding algorithms from `algorithms.py` to control Pac-Man when AI is enabled.
* **`ghost.py`**: Defines the `Ghost` class. It manages the behavior of the enemy ghosts, including their movement logic (currently a randomized walk), animation, and collision interactions with Pac-Man.
* **`berry.py`**: Defines the `Berry` class for the collectible pellets. It distinguishes between regular berries and power-up berries.
* **`cell.py`**: Defines the `Cell` class, which is used to create the wall objects that form the maze.

## AI & Pathfinding

This section details the artificial intelligence and algorithm components.

* **`algorithms.py`**: This file contains the implementations of four different pathfinding algorithms used by the AI-controlled Pac-Man:

  * Breadth-First Search (BFS)
  * Depth-First Search (DFS)
  * Uniform Cost Search (UCS)
  * A* Search (using Manhattan distance as the heuristic)

* **`options.py`**: This script runs before the main game loop to display a menu. It allows the user to select which of the four pathfinding algorithms the AI will use during the game.

## Display & Utilities

This section covers rendering and helper functions.

* **`display.py`**: This class handles rendering all the UI text and information on the screen, such as the current score, number of lives remaining, game level, and game over messages.
* **`animation.py`**: Contains the `import_sprite` utility function, which loads a sequence of images from a directory to be used for character animations.

---

# Documentation of LLM Usage

> Begin Alex's AI-Usage documentation

## 10/28/25

Models used:
Gemini CLI (2.5 Pro)

Used for:
Generating a script allowing the user to choose which algorithm PACMAN uses to plan his next move(s)
Prompt:
@options.py/ ... Write a script based on the multi-line comment in the file

\[the multi-line comment in question]

```
def show_algorithm_info():
Center a title in the render window and make the Y-top of the title 10% from the top of the window
Make a 4-line list of pathfinding algorithms to choose from which, when selected, changes PACMAN's movement:
- "Breadth-First Search"
- "Depth-First Search"
- "A* Search"
- "Uniform Cost Search"

Listen for user's key input. When the up and down arrow keys (or the W and S keys) are pressed, the menu changes selection respectively.
When an item is selected, it should be highlighted yellow with black text. Non-selected items should have white text on a black background.

Pressing ENTER should modify the ALGORITHM variable imported from settings.py previously in the script to make it whatever algorithm was selected in the list.
Pressing ENTER should begin the main game loop.
```

> End Alex's AI-Usage documentation

## 11/9/25

-Exequiel's AI-usage documentation

Models used:
Codex CLI (GPT-5 coding agent)

Used for:
Adding ghost-aware auto-pathing and reliability fixes
Prompts:

* Diagnose Pac-Man clipping through walls at higher speeds and fix the collision/raycast logic in `pac.py`.
* Investigate hesitations at corners and adjust AI replanning + target selection to keep movement smooth.
* Wire the startup algorithm picker so runtime AI uses the selected search strategy (options menu → game loop).
* Make A* (and other planners) avoid ghosts when Pac-Man isn’t powered up, including new hazard tracking and path fallbacks.
  Files/lines changed (11/9/25 session):
* `pac.py` (lines ~35-200): added ghost hazard tracking, smarter target selection, collision raycast, and fallback planning.
* `world.py` (lines ~24-165): new ghost-grid helper plus wiring to refresh Pac-Man’s hazard cache each frame.

