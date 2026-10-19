
def dfs_can_reach(maze, start, exit_room):
    visited = []

    def dfs(room):
        if room not in visited:
            visited.append(room)

            if room == exit_room:
                return True

            for neighbour in maze[room]:
                if dfs(neighbour):
                    return True

        return False

    result = dfs(start)

    print("Visit order:", visited)
    return result


maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": [],
}

result = dfs_can_reach(maze, "Entrance", "Exit")
print("Can reach Exit from Entrance?", result)
