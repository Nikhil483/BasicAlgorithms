from collections import deque


def bfs_rec(graph, visited, queue):

    if not queue:
        return

    node = queue.popleft()
    print(node, end=" ")

    for edge in graph[node] :
        if edge not in visited :
            visited.add(edge)
            queue.append(edge)

    bfs_rec(graph, visited, queue)

def bfs_recursive(graph):
    visited = set()

    for node in graph : # this loops ensure we cover all disconnected and isolated sections of a graph
        if node not in visited :
            visited.add(node)
            queue = deque([node]) # Since we identifying starting points of each connected section, we don't do append
            bfs_rec(graph, visited, queue)


def bfs_iterative(graph):

    visited = set()

    for node in graph : # Iterate over all nodes to handle disconnected components
        if node not in visited :
            visited.add(node)
            queue = deque([node]) # Initialize a queue for the BFS of this component

        while queue:
            curr_node = queue.popleft()
            print(curr_node, end=" ")

            # Add unvisited neighbors to the queue
            for edge in graph[curr_node] :
                if edge not in visited :
                    visited.add(edge)
                    queue.append(edge)


if __name__ == "__main__":

    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1, 5],
        5: [4],
        6: [7],  # Disconnected component
        7: [6],
        8: []  # Isolated node
    }

    print(graph)

    bfs_iterative(graph)
    print()
    bfs_recursive(graph)