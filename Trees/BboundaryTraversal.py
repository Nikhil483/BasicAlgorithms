from Trees.Traversals import Node


def printLeftBoundary(root):

    if root is not None:
        if root.left:
            print(root.data, end=" ")
            printLeftBoundary(root.left)

        elif root.right:
            print(root.data, end=" ")
            printLeftBoundary(root.right)


def printLeaves(root):

    if root is not None:
        printLeaves(root.left)

        if root.left is None and root.right is None:
            print(root.data, end=" ")

        printLeaves(root.right)


def printRightBoundary(root):
    if root is not None:
        if root.right:
            printRightBoundary(root.right)
            print(root.data, end=" ")

        elif root.left:
            printRightBoundary(root.left)
            print(root.data, end=" ")


def printBoundary(root):
    if root is None:
        print("No nodes to print")
        return

    # print left boundary
    printLeftBoundary(root)

    # prints leaves in lft and right subtree
    printLeaves(root.left)
    printLeaves(root.right)

    # print right
    printRightBoundary(root)



if __name__ == "__main__" :
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    printBoundary(root)