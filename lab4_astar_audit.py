
import heapq

# Campus weighted graph
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

# Supplied heuristic values
heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}


def search(graph, h, start, goal):
    counter = 0

    # Priority queue: f, g, insertion order, node, path
    frontier = [(h[start], 0, counter, start, [start])]
    best = {start: 0}

    processed = []
    expanded = []

    while frontier:
        f, g, order, node, path = heapq.heappop(frontier)

        # Ignore outdated queue entries
        if g != best.get(node):
            continue

        processed.append(node)

        # Goal is processed but not expanded
        if node == goal:
            return path, g, processed, expanded

        expanded.append(node)

        for nxt, weight in graph[node]:
            new_g = g + weight

            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                counter += 1

                new_f = new_g + h[nxt]

                heapq.heappush(
                    frontier,
                    (new_f, new_g, counter,
                     nxt, path + [nxt])
                )

    return None, None, processed, expanded


def calculate_cost(path, graph):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        for neighbour, weight in graph[current]:
            if neighbour == next_node:
                total += weight
                break

    return total


def show_results(title, result):
    path, cost, processed, expanded = result

    print("\n" + title)
    print("Returned Path:", path)
    print("Returned Cost:", cost)
    print("Independently Calculated Cost:",
          calculate_cost(path, graph))
    print("Processed Nodes:", processed)
    print("Expanded Nodes:", expanded)
    print("Expansion Count:", len(expanded))


# Experiment 1: A* with supplied heuristic
astar_result = search(graph, heuristic, "S", "G")
show_results("A* WITH SUPPLIED HEURISTIC", astar_result)


# Experiment 2: UCS using zero heuristic
zero_heuristic = {node: 0 for node in graph}

ucs_result = search(graph, zero_heuristic, "S", "G")
show_results("UCS WITH ZERO HEURISTIC", ucs_result)


# Experiment 3: Overestimate h(C) from 2 to 10
modified_heuristic = heuristic.copy()
modified_heuristic["C"] = 10

print("\nHEURISTIC OVERestimate TEST")
print("Original h(C):", heuristic["C"])
print("Modified h(C):", modified_heuristic["C"])
print("True remaining cost from C: 3")

overestimate_result = search(
    graph, modified_heuristic, "S", "G"
)

show_results("A* WITH OVERestimated h(C)", overestimate_result)
