import pygame
from dsa_logic import Stack, Queue

WIDTH, HEIGHT = 900, 650

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
GREEN = (70, 170, 100)
RED = (220, 90, 90)
BLUE = (90, 130, 220)
PURPLE = (150, 90, 210)
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


def draw_stack(screen, stack, font):
    draw_text(screen, "Stack: LIFO", font, BLACK, 120, 130)

    x = 130
    bottom = 520
    box_w = 130
    box_h = 45

    for index, value in enumerate(stack.items):
        y = bottom - (index + 1) * box_h
        pygame.draw.rect(screen, GREEN, (x, y, box_w, box_h))
        pygame.draw.rect(screen, BLACK, (x, y, box_w, box_h), 2)
        draw_text(screen, str(value), font, WHITE, x + 45, y + 10)

    draw_text(screen, "Top", font, BLACK, x + box_w + 15, bottom - len(stack.items) * box_h - 30)


def draw_queue(screen, queue, font):
    draw_text(screen, "Queue: FIFO", font, BLACK, 520, 130)

    x = 470
    y = 310
    box_w = 70
    box_h = 55

    for index, value in enumerate(list(queue.items)):
        box_x = x + index * box_w
        pygame.draw.rect(screen, PURPLE, (box_x, y, box_w, box_h))
        pygame.draw.rect(screen, BLACK, (box_x, y, box_w, box_h), 2)
        draw_text(screen, str(value), font, WHITE, box_x + 22, y + 15)

    draw_text(screen, "Front", font, BLACK, x, y + 80)
    draw_text(screen, "Rear", font, BLACK, x + max(len(queue.items)-1, 0) * box_w, y - 35)


def run_data_structures(screen):
    pygame.display.set_caption("Data Structures Playground")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont(None, 46)
    font = pygame.font.SysFont(None, 28)

    stack = Stack()
    queue = Queue()
    counter = 1

    buttons = {
        "Push": pygame.Rect(80, 560, 100, 45),
        "Pop": pygame.Rect(200, 560, 100, 45),
        "Enqueue": pygame.Rect(500, 560, 120, 45),
        "Dequeue": pygame.Rect(640, 560, 120, 45),
        "Back": pygame.Rect(20, 20, 90, 40),
    }

    running = True
    while running:
        screen.fill(WHITE)

        draw_text(screen, "Module 1: Data Structures Playground", title_font, BLACK, 160, 35)
        draw_text(screen, "Stack uses push/pop. Queue uses enqueue/dequeue.", font, BLACK, 210, 85)

        draw_stack(screen, stack, font)
        draw_queue(screen, queue, font)

        for text, rect in buttons.items():
            draw_button(screen, text, rect, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if buttons["Back"].collidepoint(pos):
                    running = False

                elif buttons["Push"].collidepoint(pos):
                    stack.push(counter)
                    counter += 1

                elif buttons["Pop"].collidepoint(pos):
                    stack.pop()

                elif buttons["Enqueue"].collidepoint(pos):
                    queue.enqueue(counter)
                    counter += 1

                elif buttons["Dequeue"].collidepoint(pos):
                    queue.dequeue()

        pygame.display.flip()
        clock.tick(60)
