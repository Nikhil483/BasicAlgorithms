def dfs_iterative(graph):

    visited = set()
    stack = []

    for node in graph:
        if node not in visited :
            # visited.add(node) -
            # can't mark visited here because nodes are processed when items are popped from stack, not before adding
            stack.append(node)

        while stack :
            curr_node = stack.pop()
            if curr_node not in visited :
                visited.add(curr_node)
                print(curr_node, end = " ")

                # for loop is inside of if, because we only need to push edges of nodes which have not already been visited
                for edge in graph[curr_node]:
                    if edge not in visited :
                        visited.add(edge)
                        stack.append(edge)


def dfs_rec(graph, visited, node):

    visited.add(node)
    print(node, end=" ")

    for edge in graph[node]:
        if edge not in visited :
            # this all ensures depth first principle because instead of traversing all edges from a node,
            # we call dfs on every edge we see, this make the algo to go deeper into graph
            # whereas in BFS we append edges to end and come back for them only after all the current edges are processed
            dfs_rec(graph, visited, edge)


def dfs_recursive(graph):
    visited = set()

    for node in graph :
        if node not in visited :
            dfs_rec(graph, visited, node)


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

    dfs_iterative(graph)
    print()
    dfs_recursive(graph)