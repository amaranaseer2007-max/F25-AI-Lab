
import heapq

# Weighted graph
# Each connection has a travel cost.
graph = {
    "A": [("B", 1), ("C", 6)],
    "B": [("D", 4), ("E", 1)],
    "C": [("F", 8), ("G", 6)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}


def bfs(start, goal):
    queue = [(start, [start])]
    seen = {start}
    processed = []

    while queue:
        node, path = queue.pop(0)
        processed.append(node)

        if node == goal:
            return path, processed

        for neighbour, weight in graph[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None, processed


def ucs(start, goal, search_graph):
    frontier = [(0, 0, start, [start])]
    best_cost = {start: 0}
    processed = []
    counter = 1

    while frontier:
        cost, _, node, path = heapq.heappop(frontier)

        if cost != best_cost.get(node):
            continue

        processed.append(node)

        if node == goal:
            return path, cost, processed

        for neighbour, weight in search_graph[node]:
            new_cost = cost + weight

            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost

                heapq.heappush(
                    frontier,
                    (new_cost, counter, neighbour,
                     path + [neighbour])
                )
                counter += 1

    return None, None, processed


def calculate_cost(path, search_graph):
    total = 0

    for i in range(len(path) - 1):
        for neighbour, weight in search_graph[path[i]]:
            if neighbour == path[i + 1]:
                total += weight
                break

    return total


# Compare BFS and UCS
bfs_path, bfs_order = bfs("A", "G")
ucs_path, ucs_cost, ucs_order = ucs("A", "G", graph)

print("BFS Path:", bfs_path)
print("BFS Visit Order:", bfs_order)
print("BFS Total Cost:", calculate_cost(bfs_path, graph))

print("\nUCS Path:", ucs_path)
print("UCS Processing Order:", ucs_order)
print("UCS Total Cost:", ucs_cost)

print("Independently Calculated Cost:",
      calculate_cost(ucs_path, graph))


# Edge-case tests
print("\nEDGE CASE TESTS")

print("Start equals goal:", ucs("A", "A", graph)[:2])

unreachable_graph = {
    "A": [("B", 1)],
    "B": [],
    "G": []
}
print("Unreachable goal:",
      ucs("A", "G", unreachable_graph)[:2])

cycle_graph = {
    "A": [("B", 1)],
    "B": [("A", 1), ("G", 2)],
    "G": []
}
print("Graph with cycle:", ucs("A", "G", cycle_graph)[:2])
