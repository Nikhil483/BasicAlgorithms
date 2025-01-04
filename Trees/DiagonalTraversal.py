from Trees.Traversals import Node, BinaryTree
from collections import deque

def diagonal_traversal(node, q = deque(), first_time = True):
    if first_time: q.append(node)

    while node is not None and len(q) > 0:
        if node.left is not None:
            q.append(node.left)

        print(node.data, end = " ")
        node = node.right

    q.popleft()
    if len(q) > 0:
        diagonal_traversal(q[0],q, False)

if __name__ == "__main__":
    b_tree = BinaryTree()
    n8 = Node(8)
    n1 = Node(1)
    n3 = Node(3)
    n4 = Node(4)
    n10 = Node(10)
    n14 = Node(14)
    n13 = Node(13)
    n6 = Node(6)
    n7 = Node(7)

    b_tree.root = n8
    n8.left, n8.right = n3, n10
    n3.left, n3.right = n1, n6
    n6.left, n6.right = n4, n7
    n10.right = n14
    n14.left = n13

    b_tree.print_tree(b_tree.root)

    diagonal_traversal(b_tree.root)

