
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path

    depth = len(path) - 1

    if depth == limit:
        for neighbour in graph[node]:
            if neighbour not in path:
                return "CUTOFF", None
        return "FAILURE", None

    cutoff_found = False

    for neighbour in graph[node]:
        if neighbour not in path:
            status, result = dls(
                neighbour, goal, limit, path + [neighbour]
            )

            if status == "FOUND":
                return status, result

            if status == "CUTOFF":
                cutoff_found = True

    if cutoff_found:
        return "CUTOFF", None

    return "FAILURE", None


def iddfs(start, goal, max_depth):
    attempted_limits = []

    for limit in range(1, max_depth + 1):
        attempted_limits.append(limit)

        status, path = dls(start, goal, limit, [start])

        if status == "FOUND":
            return status, path, attempted_limits

        if status == "FAILURE":
            return status, None, attempted_limits

    return "CUTOFF", None, attempted_limits


print("DLS RESULTS")

for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])
    print("Limit:", limit, "| Status:", status, "| Path:", path)


print("\nIDDFS RESULTS")

for max_depth in [1, 2, 3, 4]:
    status, path, attempts = iddfs("A", "G", max_depth)

    print("Maximum depth:", max_depth)
    print("Status:", status)
    print("Path:", path)
    print("Limits attempted:", attempts)
    print()
