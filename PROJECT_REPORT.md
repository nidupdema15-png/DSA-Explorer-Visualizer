# DSA Explorer and Visualiser App - Project Report

## 1. Introduction

The DSA Explorer and Visualiser App is an interactive Python application developed using PyGame. The purpose of this project is to help users understand data structures and algorithms through visual and interactive demonstrations.

The project focuses on three main modules: a Data Structures Playground, a Sorting Visualiser, and a Graph Traversal Visualiser. Each module includes interactive controls and visual feedback so users can observe how the algorithms work step-by-step.

---

## 2. Project Overview

The project combines multiple algorithm visualisations into one modular application. The main menu allows the user to choose between different modules.

The three implemented modules are:

1. Data Structures Playground
2. Sorting Visualiser
3. Graph Traversal Visualiser

Each module demonstrates at least two data structure or algorithm concepts and includes automated testing for the underlying logic.

---

## 3. App Design and Layout

The app begins with a main menu containing buttons for each module. The user can select a module and interact with its controls.

The layout includes:
- A main menu screen
- Individual PyGame screens for each module
- Buttons for user interaction
- Visual animations and status text
- A back button to return to the main menu

This modular layout makes the app easier to maintain and extend in the future.

---

## 4. Module 1: Data Structures Playground

### Description

The Data Structures Playground demonstrates Stack and Queue operations.

### Stack

A stack follows the LIFO principle, which means Last In, First Out. In the app, the user can push items onto the stack and pop items from the top.

### Queue

A queue follows the FIFO principle, which means First In, First Out. In the app, the user can enqueue items to the rear of the queue and dequeue items from the front.

### Features

- Push button for stack
- Pop button for stack
- Enqueue button for queue
- Dequeue button for queue
- Visual display of stack and queue elements

### Testing

The stack and queue were tested using unittest. The tests confirm that stack pop removes the most recent item and queue dequeue removes the earliest item.

---

## 5. Module 2: Sorting Visualiser

### Description

The Sorting Visualiser demonstrates two sorting algorithms: Bubble Sort and Selection Sort.

### Bubble Sort

Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. Larger values gradually move toward the end of the list.

### Selection Sort

Selection sort repeatedly finds the smallest remaining element and places it in the correct position.

### Features

- Random array generation
- Bubble sort animation
- Selection sort animation
- Highlighted compared elements
- Step-by-step bar visualisation

### Testing

The sorting algorithms were tested by checking whether the final array produced by each algorithm is sorted correctly.

---

## 6. Module 3: Graph Traversal Visualiser

### Description

The Graph Traversal Visualiser demonstrates Breadth First Search and Depth First Search.

### BFS

Breadth First Search explores nodes level by level. It uses a queue to decide which node to visit next.

### DFS

Depth First Search explores as far as possible along one path before backtracking. It can be implemented using a stack.

### Features

- Interactive graph with clickable nodes
- User-selected start node
- BFS animation
- DFS animation
- Traversal order display

### Testing

The graph traversal logic was tested using unittest. The tests confirm that BFS and DFS visit the expected nodes in the correct order.

---

## 7. Automated Test Cases

| Module | Test Case | Expected Result |
|---|---|---|
| Data Structures | Stack push/pop | Last inserted item is removed first |
| Data Structures | Queue enqueue/dequeue | First inserted item is removed first |
| Sorting | Bubble sort | Final array is sorted |
| Sorting | Selection sort | Final array is sorted |
| Graph | BFS from A | Nodes are visited in BFS order |
| Graph | DFS from A | Nodes are visited in DFS order |

---

## 8. Problems Faced and Solutions

One challenge was separating the visual PyGame code from the algorithm logic. This was solved by placing the main algorithm and data structure logic inside `dsa_logic.py`. This made testing easier because the tests can run without opening the PyGame windows.

Another challenge was showing algorithms step-by-step. This was solved by creating lists of algorithm steps for sorting and graph traversal. PyGame then displays one step at a time.

---

## 9. Conclusion

The DSA Explorer and Visualiser App successfully demonstrates important data structure and algorithm concepts through interactive PyGame visualisation. The application is modular, tested, and easy to expand with additional features such as linked lists, binary search trees, heaps, and pathfinding puzzles.

---

## 10. GitHub Link

Add your GitHub repository link here after uploading the project:

`https://github.com/your-username/DSA_Explorer`
