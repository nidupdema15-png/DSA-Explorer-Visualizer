from collections import deque

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.popleft()

    def size(self):
        return len(self.items)


def bubble_sort_steps(array):
    arr = array[:]
    steps = []
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append((arr[:], j, j + 1, False))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append((arr[:], j, j + 1, True))

    steps.append((arr[:], -1, -1, False))
    return steps


def selection_sort_steps(array):
    arr = array[:]
    steps = []
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            steps.append((arr[:], min_index, j, False))
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            steps.append((arr[:], i, min_index, True))

    steps.append((arr[:], -1, -1, False))
    return steps


GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


def bfs(graph, start):
    visited = []
    queue = deque([start])
    seen = {start}

    while queue:
        node = queue.popleft()
        visited.append(node)

        for neighbour in graph[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)

    return visited


def dfs(graph, start):
    visited = []
    stack = [start]
    seen = set()

    while stack:
        node = stack.pop()

        if node not in seen:
            seen.add(node)
            visited.append(node)

            for neighbour in reversed(graph[node]):
                if neighbour not in seen:
                    stack.append(neighbour)

    return visited
