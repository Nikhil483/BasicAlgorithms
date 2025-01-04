from re import search

from Trees.Traversals import BinaryTree, Node


def searchBST(root, value) :
    curr = root

    while curr is not None:
        if curr.data == value :
            return True
        elif curr.data < value :
            curr = curr.right
        else :
            curr = curr.left


if __name__ == "__main__" :
    b = BinaryTree()
    n = Node(1)
    n1 = Node(2)
    n2 = Node(3)
    n3 = Node(4)
    n4 = Node(5)
    n5 = Node(6)
    n6 = Node(7)

    b.root = n3
    b.root.left = n2
    b.root.right = n4
    n2.left = n
    n2.right = n1
    n4.left = n5
    n4.right = n6

    b.print_tree(b.root)

    to_search = 1
    if searchBST(b.root, to_search) :
        print("Element " + str(to_search) + " Found")
    else :
        print("Element is not found")