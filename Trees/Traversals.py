class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def print_tree(self, node, count=0, is_left=False):
        if node is None:
             return

        self.print_tree(node.right, count + 1)
        indent = " " * 4 * count
        branch = "|____" if is_left else "|````" if count > 0 else ""

        print(f"{indent}{branch}{node.data}")
        self.print_tree(node.left, count + 1, True)


def in_order_traversal(node):
    # left root right
    if node is None :
        return
    in_order_traversal(node.left)
    print(node.data, end=" ")
    in_order_traversal(node.right)


def pre_order_traversal(node):
    # root left right
    if node is None:
        return
    print(node.data, end=" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


def post_order_traversal(node):
    # left right root
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=" ")


def in_order_traversal_iterative(root):
    stack = []
    ans = []
    node = root

    while node is not None or len(stack) > 0:

        # Keep going left and keep track of nodes in stack
        while node is not None :
            stack.append(node)
            node = node.left

        # once left node doesn't have child nodes pop and print
        node = stack.pop()
        ans.append(node.data)

        # move on to right node
        node = node.right
    return ans

def pre_order_traversal_iterative(root):
    stack = []
    ans = []
    node = root

    while node is not None or len(stack) > 0:

        # Keep going left and keep track of nodes in stack
        while node is not None:
            stack.append(node)
            # ans keeps order intact, while stack pop is required to keep track of visited nodes
            ans.append(node.data)
            node = node.left

        # once left node doesn't have child nodes pop and print
        node = stack.pop()

        # move on to right node
        node = node.right
    return ans


if __name__ == "__main__" :
    b = BinaryTree()
    n = Node(1)
    n1 = Node(2)
    n2 = Node(3)
    n3 = Node(4)
    n4 = Node(5)
    n5 = Node(6)
    n6 = Node(7)

    b.root = n
    b.root.left = n1
    b.root.right = n2
    n2.left = n3
    n2.right = n4
    n1.left = n5
    n1.right = n6

    b.print_tree(b.root)

    print("\nIn-order traversal : ", end="")
    in_order_traversal(b.root)

    print("\nPre-order traversal : ", end="")
    pre_order_traversal(b.root)

    print("\nPost-order traversal : ", end="")
    post_order_traversal(b.root)

    print("\n\nIn-order traversal iterative  : " + str(in_order_traversal_iterative(b.root)))
    print("Pre-order traversal iterative  : " + str(pre_order_traversal_iterative(b.root)))
    # print("Post-order traversal iterative  : " + str(post_order_traversal_iterative(b.root)))
