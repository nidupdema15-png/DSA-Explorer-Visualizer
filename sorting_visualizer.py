import pygame
import random
from dsa_logic import bubble_sort_steps, selection_sort_steps

WIDTH, HEIGHT = 900, 650

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
BLUE = (90, 130, 220)
GREEN = (80, 180, 110)
RED = (220, 90, 90)
ORANGE = (240, 170, 70)
GRAY = (210, 210, 210)


def draw_text(screen, text, font, colour, x, y):
    surface = font.render(text, True, colour)
    screen.blit(surface, (x, y))


def draw_button(screen, text, rect, font):
    pygame.draw.rect(screen, BLUE, rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=10)
    label = font.render(text, True, WHITE)
    screen.blit(label, (rect.centerx - label.get_width() // 2,
                        rect.centery - label.get_height() // 2))


def draw_bars(screen, array, compare_a, compare_b, font):
    start_x = 100
    base_y = 530
    bar_width = 45
    gap = 15
    max_value = max(array)

    for i, value in enumerate(array):
        height = int((value / max_value) * 330)
        x = start_x + i * (bar_width + gap)
        y = base_y - height

        colour = ORANGE if i in (compare_a, compare_b) else GREEN
        pygame.draw.rect(screen, colour, (x, y, bar_width, height))
        pygame.draw.rect(screen, BLACK, (x, y, bar_width, height), 2)
        draw_text(screen, str(value), font, BLACK, x + 10, base_y + 10)


def new_array():
    return random.sample(range(10, 100), 10)


def run_sorting_visualizer(screen):
    pygame.display.set_caption("Sorting Visualiser")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont(None, 46)
    font = pygame.font.SysFont(None, 27)

    array = new_array()
    steps = []
    step_index = 0
    running_sort = False
    algorithm_name = "None"

    buttons = {
        "Bubble Sort": pygame.Rect(80, 570, 140, 45),
        "Selection Sort": pygame.Rect(240, 570, 160, 45),
        "Random": pygame.Rect(420, 570, 120, 45),
        "Back": pygame.Rect(20, 20, 90, 40),
    }

    running = True
    while running:
        screen.fill(WHITE)

        draw_text(screen, "Module 2: Sorting Visualiser", title_font, BLACK, 220, 35)
        draw_text(screen, f"Current algorithm: {algorithm_name}", font, BLACK, 320, 90)
        draw_text(screen, "Orange bars are being compared/swapped.", font, BLACK, 260, 120)

        compare_a, compare_b = -1, -1
        if steps and step_index < len(steps):
            current_array, compare_a, compare_b, swapped = steps[step_index]
            array = current_array[:]

        draw_bars(screen, array, compare_a, compare_b, font)

        for text, rect in buttons.items():
            draw_button(screen, text, rect, font)

        if running_sort and steps:
            step_index += 1
            if step_index >= len(steps):
                running_sort = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if buttons["Back"].collidepoint(pos):
                    running = False

                elif buttons["Bubble Sort"].collidepoint(pos):
                    steps = bubble_sort_steps(array)
                    step_index = 0
                    running_sort = True
                    algorithm_name = "Bubble Sort"

                elif buttons["Selection Sort"].collidepoint(pos):
                    steps = selection_sort_steps(array)
                    step_index = 0
                    running_sort = True
                    algorithm_name = "Selection Sort"

                elif buttons["Random"].collidepoint(pos):
                    array = new_array()
                    steps = []
                    step_index = 0
                    running_sort = False
                    algorithm_name = "None"

        pygame.display.flip()
        clock.tick(8)
