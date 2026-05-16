# DSA Explorer and Visualiser App

## Project Overview
This project is an interactive Data Structures and Algorithms Explorer and Visualiser built using Python and PyGame. The aim of the app is to help users understand common data structures and algorithms through animations, buttons, and interactive visual elements.

The app contains three fully implemented modules:

1. Data Structures Playground
2. Sorting Visualiser
3. Graph Traversal Visualiser

Each module demonstrates at least two data structure or algorithm concepts using PyGame visualisation.

## Implemented Modules

### Module 1: Data Structures Playground

This module demonstrates Stack and Queue operations.

#### Stack
A stack follows the LIFO principle, which means Last In, First Out. The last item pushed into the stack is the first item removed.

Implemented operations:
- Push
- Pop

#### Queue
A queue follows the FIFO principle, which means First In, First Out. The first item added to the queue is the first item removed.

Implemented operations:
- Enqueue
- Dequeue

### Module 2: Sorting Visualiser

This module demonstrates sorting algorithms using animated bars.

Implemented algorithms:
- Bubble Sort
- Selection Sort

The app highlights compared elements and shows the array changing step-by-step.

### Module 3: Graph Traversal Visualiser

This module demonstrates graph traversal algorithms.

Implemented algorithms:
- Breadth First Search (BFS)
- Depth First Search (DFS)

The user can click a start node and then choose BFS or DFS. The traversal order is animated and displayed on the screen.

## How to Run the App

Install PyGame:

```bash
pip install pygame
```

Run the app:

```bash
python main.py
```

## How to Run Tests

From the project folder, run:

```bash
python -m unittest discover tests
```

## Files

```text
main.py
data_structures.py
sorting_visualizer.py
graph_visualizer.py
dsa_logic.py
tests/test_stack_queue.py
tests/test_sorting.py
tests/test_graph.py
```

---

## Testing Summary

Automated testing was completed using Python's unittest module.

The tests validate:
- Stack push and pop behaviour
- Queue enqueue and dequeue behaviour
- Bubble sort correctness
- Selection sort correctness
- BFS traversal correctness
- DFS traversal correctness


## Conclusion
The DSA Explorer and Visualiser App successfully demonstrates key data structures and algorithms using interactive PyGame visualisations. The project is modular, tested, and easy to extend with more modules such as linked lists, binary search trees, heaps, and pathfinding puzzles.
