
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def bfs(start, goal):
    queue = deque([(start, [start])])
    seen = {start}
    processed = []

    while queue:
        node, path = queue.popleft()
        processed.append(node)

        if node == goal:
            return path, processed

        for neighbour in graph[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None, processed


def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()
    processed = []

    while stack:
        node, path = stack.pop()

        if node in seen:
            continue

        seen.add(node)
        processed.append(node)

        if node == goal:
            return path, processed

        for neighbour in reversed(graph[node]):
            if neighbour not in seen:
                stack.append((neighbour, path + [neighbour]))

    return None, processed


bfs_path, bfs_order = bfs("A", "G")
dfs_path, dfs_order = dfs("A", "G")

print("BFS Path:", bfs_path)
print("BFS Visit Order:", bfs_order)

print("\nDFS Path:", dfs_path)
print("DFS Visit Order:", dfs_order)
