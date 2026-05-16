import pygame
import sys

from data_structures import run_data_structures
from sorting_visualizer import run_sorting_visualizer
from graph_visualizer import run_graph_visualizer

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DSA Explorer and Visualiser App")

FONT_TITLE = pygame.font.SysFont(None, 52)
FONT = pygame.font.SysFont(None, 34)

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
BLUE = (90, 130, 220)
LIGHT_BLUE = (160, 190, 255)
GRAY = (220, 220, 220)


def draw_text(text, font, colour, x, y):
    surface = font.render(text, True, colour)
    screen.blit(surface, (x, y))


def draw_button(text, rect):
    mouse_pos = pygame.mouse.get_pos()
    colour = LIGHT_BLUE if rect.collidepoint(mouse_pos) else BLUE
    pygame.draw.rect(screen, colour, rect, border_radius=12)
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=12)

    label = FONT.render(text, True, WHITE)
    screen.blit(label, (rect.centerx - label.get_width() // 2,
                        rect.centery - label.get_height() // 2))


def main_menu():
    clock = pygame.time.Clock()

    buttons = {
        "Data Structures": pygame.Rect(320, 180, 260, 60),
        "Sorting": pygame.Rect(320, 270, 260, 60),
        "Graphs": pygame.Rect(320, 360, 260, 60),
        "Quit": pygame.Rect(320, 450, 260, 60),
    }

    running = True
    while running:
        screen.fill(WHITE)

        draw_text("DSA Explorer and Visualiser App", FONT_TITLE, BLACK, 145, 70)
        draw_text("Choose a module to explore", FONT, BLACK, 300, 125)

        for name, rect in buttons.items():
            draw_button(name, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if buttons["Data Structures"].collidepoint(pos):
                    run_data_structures(screen)

                elif buttons["Sorting"].collidepoint(pos):
                    run_sorting_visualizer(screen)

                elif buttons["Graphs"].collidepoint(pos):
                    run_graph_visualizer(screen)

                elif buttons["Quit"].collidepoint(pos):
                    running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_menu()
