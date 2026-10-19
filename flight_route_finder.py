
def path_cost(path):
    return sum(cost for _, cost in path)


def ucs_cheapest_route(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    explored_count = 0

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]

        explored_count += 1
        route = [city for city, cost in path]
        cost = path_cost(path)
        print("Exploring route:", route, "| Cost:", cost)

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            print("Cheapest route:", route)
            print("Total ticket cost:", cost)
            print("Total routes explored:", explored_count)
            return route, cost

        for neighbour, ticket_price in graph.get(node, []):
            if neighbour not in visited:
                queue.append(path + [(neighbour, ticket_price)])

    print("No route found.")
    print("Total routes explored:", explored_count)
    return None, None


flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": [],
}

ucs_cheapest_route(flights, "Islamabad", "Quetta")
