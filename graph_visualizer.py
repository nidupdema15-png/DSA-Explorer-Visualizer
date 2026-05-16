import pygame
from dsa_logic import GRAPH, bfs, dfs

WIDTH, HEIGHT = 900, 650

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
BLUE = (90, 130, 220)
GREEN = (80, 180, 110)
RED = (220, 90, 90)
YELLOW = (250, 220, 90)
GRAY = (200, 200, 200)


POSITIONS = {
    "A": (450, 150),
    "B": (280, 280),
    "C": (620, 280),
    "D": (180, 450),
    "E": (380, 450),
    "F": (620, 450),
}


def draw_text(screen, text, font, colour, x, y):
    surface = font.render(text, True, colour)
    screen.blit(surface, (x, y))


def draw_button(screen, text, rect, font):
    pygame.draw.rect(screen, BLUE, rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=10)
    label = font.render(text, True, WHITE)
    screen.blit(label, (rect.centerx - label.get_width() // 2,
                        rect.centery - label.get_height() // 2))


def draw_graph(screen, visited_nodes, current_node, selected_node, font):
    drawn_edges = set()

    for node, neighbours in GRAPH.items():
        x1, y1 = POSITIONS[node]
        for neighbour in neighbours:
            edge = tuple(sorted((node, neighbour)))
            if edge not in drawn_edges:
                x2, y2 = POSITIONS[neighbour]
                pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 3)
                drawn_edges.add(edge)

    for node, (x, y) in POSITIONS.items():
        colour = GRAY

        if node in visited_nodes:
            colour = GREEN
        if node == current_node:
            colour = YELLOW
        if node == selected_node:
            colour = RED

        pygame.draw.circle(screen, colour, (x, y), 32)
        pygame.draw.circle(screen, BLACK, (x, y), 32, 3)

        label = font.render(node, True, BLACK)
        screen.blit(label, (x - label.get_width() // 2, y - label.get_height() // 2))


def get_clicked_node(pos):
    mouse_x, mouse_y = pos

    for node, (x, y) in POSITIONS.items():
        distance = ((mouse_x - x) ** 2 + (mouse_y - y) ** 2) ** 0.5
        if distance <= 32:
            return node

    return None


def run_graph_visualizer(screen):
    pygame.display.set_caption("Graph Traversal Visualiser")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont(None, 46)
    font = pygame.font.SysFont(None, 27)

    selected_node = "A"
    traversal_order = []
    visited_nodes = []
    step_index = 0
    running_traversal = False
    algorithm_name = "None"

    buttons = {
        "BFS": pygame.Rect(250, 570, 100, 45),
        "DFS": pygame.Rect(370, 570, 100, 45),
        "Reset": pygame.Rect(490, 570, 100, 45),
        "Back": pygame.Rect(20, 20, 90, 40),
    }

    running = True
    while running:
        screen.fill(WHITE)

        draw_text(screen, "Module 3: Graph Traversal Visualiser", title_font, BLACK, 160, 35)
        draw_text(screen, "Click a node to choose a start node. Then press BFS or DFS.", font, BLACK, 185, 85)
        draw_text(screen, f"Selected start node: {selected_node}", font, BLACK, 330, 115)
        draw_text(screen, f"Algorithm: {algorithm_name}", font, BLACK, 370, 140)

        current_node = None
        if running_traversal and step_index < len(traversal_order):
            current_node = traversal_order[step_index]
            if current_node not in visited_nodes:
                visited_nodes.append(current_node)
            step_index += 1
        elif step_index >= len(traversal_order):
            running_traversal = False

        draw_graph(screen, visited_nodes, current_node, selected_node, font)

        draw_text(screen, "Traversal order: " + " -> ".join(visited_nodes), font, BLACK, 170, 520)

        for text, rect in buttons.items():
            draw_button(screen, text, rect, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                clicked_node = get_clicked_node(pos)

                if clicked_node is not None:
                    selected_node = clicked_node
                    visited_nodes = []
                    traversal_order = []
                    step_index = 0
                    running_traversal = False
                    algorithm_name = "None"

                elif buttons["Back"].collidepoint(pos):
                    running = False

                elif buttons["BFS"].collidepoint(pos):
                    traversal_order = bfs(GRAPH, selected_node)
                    visited_nodes = []
                    step_index = 0
                    running_traversal = True
                    algorithm_name = "BFS"

                elif buttons["DFS"].collidepoint(pos):
                    traversal_order = dfs(GRAPH, selected_node)
                    visited_nodes = []
                    step_index = 0
                    running_traversal = True
                    algorithm_name = "DFS"

                elif buttons["Reset"].collidepoint(pos):
                    visited_nodes = []
                    traversal_order = []
                    step_index = 0
                    running_traversal = False
                    algorithm_name = "None"

        pygame.display.flip()
        clock.tick(2)
