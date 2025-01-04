def addEdge(adjList, src, dest):
    adjList[src].append(dest)


def transpose(adjList, v):
    transList = [[] for i in range(v)]
    for i in range(v):
        for node in adjList[i] :
            transList[node].append(i)
    return transList


if __name__ == "__main__" :

    v = 7
    adjList = [[] for i in range(v)]

    # basic assumption here is nodes are represented based zero index based system
    # if nodes are identified by non-zero or non-contiguous system, then a dictionary would be required
    addEdge(adjList, 0, 1)
    addEdge(adjList, 1, 2)
    addEdge(adjList, 1, 6)
    addEdge(adjList, 2, 3)
    addEdge(adjList, 2, 4)
    addEdge(adjList, 3, 1)
    addEdge(adjList, 4, 5)
    addEdge(adjList, 6, 5)

    print(adjList)

    print(transpose(adjList, v))