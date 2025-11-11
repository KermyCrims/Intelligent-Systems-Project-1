Base PacMan game taken from https://github.com/x4nth055/pythoncode-tutorials.git

All AI-generated code is marked with comments before and after it along with the date the AI wrote it on.

# AI Concepts Implemented

# Algorithm Choices and Justification

# Challenges Faced and Solutions

# Documentation of LLM Usage
---

> Begin Alex's AI-Usage documentation
## 10/28/25

Models used:
	Gemini CLI (2.5 Pro)

Used for:
	Generating a script allowing the user to choose which algorithm PACMAN uses to plan his next move(s)
	Prompt:
		@options.py/ ... Write a script based on the multi-line comment in the file
		
	[the multi-line comment in question]
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
		- Diagnose Pac-Man clipping through walls at higher speeds and fix the collision/raycast logic in `pac.py`.
		- Investigate hesitations at corners and adjust AI replanning + target selection to keep movement smooth.
		- Wire the startup algorithm picker so runtime AI uses the selected search strategy (options menu → game loop).
		- Make A* (and other planners) avoid ghosts when Pac-Man isn’t powered up, including new hazard tracking and path fallbacks.
	Files/lines changed (11/9/25 session):
		- `pac.py` (lines ~35-200): added ghost hazard tracking, smarter target selection, collision raycast, and fallback planning.
		- `world.py` (lines ~24-165): new ghost-grid helper plus wiring to refresh Pac-Man’s hazard cache each frame.
