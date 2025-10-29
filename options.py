import pygame, sys
import settings

from settings import WIDTH, HEIGHT

def show_algorithm_info():
    # **********************************************
    # * 10/28/2025 AI-Generated script begins here *
    # **********************************************
    screen = pygame.display.get_surface()
    algorithm_values = ["Breadth-First Search", "Depth-First Search", "A* Search", "Uniform Cost Search"]
    selected_index = 0

    title_font = pygame.font.Font(None, 74)
    item_font = pygame.font.Font(None, 50)

    while True:
        screen.fill("black")

        # Draw title
        title_surface = title_font.render("AUTO-PACMAN", True, "yellow") # AI-title 'PACMAN PATHFINDING' changed by Alex to "AUTO-PACMAN" 10/28/25
        title_rect = title_surface.get_rect(center=(WIDTH / 2, HEIGHT * 0.1))
        screen.blit(title_surface, title_rect)

        # Draw algorithm list
        for i, algo in enumerate(algorithm_values):
            if i == selected_index:
                text_surface = item_font.render(algo, True, "black", "yellow")
            else:
                text_surface = item_font.render(algo, True, "white")
            
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT * 0.3 + i * 60))
            screen.blit(text_surface, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    selected_index = (selected_index - 1) % len(algorithm_values)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    selected_index = (selected_index + 1) % len(algorithm_values)
                elif event.key == pygame.K_RETURN:
                    settings.ALGORITHM = algorithm_values[selected_index]
                    return # Exit the options menu

# ***********************************
# * AI-Generated script ends here *
# ***********************************
