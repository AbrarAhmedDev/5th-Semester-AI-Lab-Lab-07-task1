
def bfs_shortest_path(graph, start, goal):
    visited = [start]
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                new_path = path + [neighbour]
                queue.append(new_path)

    return None


network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara", "Ahmed"],
    "Ahmed": ["Hira"],
}

path = bfs_shortest_path(network, "Ali", "Hira")

if path:
    print("Shortest chain from Ali to Hira:", path)
    print("Number of introductions needed:", len(path) - 1)
else:
    print("No connection found.")
