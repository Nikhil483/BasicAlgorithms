from Trees.Traversals import Node, BinaryTree
from sorting.MergeSort import MergeSort


def get_nodes_into_array_in_order(root):
    stack = []
    ans = []
    node = root

    while node is not None or len(stack) > 0:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        ans.append(node.data)

        node = node.right
    return ans


def insert_values_into_tree_in_order(root, node_values_in_array):
    stack = []
    counter = len(node_values_in_array)
    index = 0
    node = root

    while (node is not None or len(stack) > 0) and index < counter:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        # in in-order traversal we append values here, for our case
        # there is no point in preserving values as we refer to them by object ref
        # values can simply be overridden at this point
        # so instead of storing the value just update it elements from sorted list
        node.data = node_values_in_array[index]
        index += 1

        node = node.right


def convert_binary_tree_to_BST(root):
    node_values_in_array = get_nodes_into_array_in_order(root)
    MergeSort().merge_sort(node_values_in_array)
    insert_values_into_tree_in_order(root, node_values_in_array)


if __name__ == "__main__" :
    b_tree = BinaryTree()
    n1 = Node(3)
    b_tree.root = n1
    n2 = Node(2)
    n3 = Node(4)
    n4 = Node(5)
    n5 = Node(6)
    n6 = Node(7)
    n7 = Node(8)

    n1.left = n2
    n1.right = n5
    n2.left = n6
    n2.right = n7
    n5.left = n3
    n5.right = n4

    b_tree.print_tree(n1)

    convert_binary_tree_to_BST(b_tree.root)
    b_tree.print_tree(n1)