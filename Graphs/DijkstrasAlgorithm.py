import heapq


def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding the shortest paths from a start node to all other nodes in a weighted graph.

    :param graph: A dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
    :param start: The starting node.
    :return: A tuple containing two dictionaries:
             - distances: shortest distance from the start node to each node.
             - previous: previous node in the shortest path to each node.
    """
    # Priority queue to hold nodes to explore
    priority_queue = []
    # Distances to all nodes initialized to infinity
    distances = {node: float('inf') for node in graph}
    # Previous nodes in the shortest path
    previous = {node: None for node in graph}
    # Distance to the start node is 0
    distances[start] = 0
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip nodes that have already been processed with a shorter path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


# Example usage
if __name__ == "__main__":
    # Graph as an adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)],
    }

    start_node = 'A'
    distances, previous = dijkstra(graph, start_node)

    print("Shortest distances:", distances)
    print("Previous nodes:", previous)
