import heapq


def greedy_best_first_search(graph, heuristics, start, goal):
    # Priority queue to store nodes to explore; heapq ensures the node with the lowest heuristic is explored first
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start], start))  # (heuristic, node)

    # To keep track of visited nodes
    visited = set()

    # To reconstruct the path
    parent = {start: None}

    while priority_queue:
        # Pop the node with the smallest heuristic value
        _, current_node = heapq.heappop(priority_queue)

        # If we reach the goal, stop the search
        if current_node == goal:
            break

        # If already visited, skip it
        if current_node in visited:
            continue

        # Mark current node as visited
        visited.add(current_node)

        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                parent[neighbor] = current_node  # Track the path
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

    # Reconstruct the path from goal to start
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent.get(node)

    path.reverse()  # Reverse the path to get start to goal
    return path


# Sample graph representing a city map (nodes are city intersections)
city_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

# Heuristic values (straight-line distance to goal 'G')
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 4,
    'F': 1,
    'G': 0
}

# Run the algorithm from node A to G
start_node = 'A'
goal_node = 'G'
path = greedy_best_first_search(city_graph, heuristics, start_node, goal_node)

# Display the result
print("Shortest path using Greedy Best First Search:")
print(" -> ".join(path))
