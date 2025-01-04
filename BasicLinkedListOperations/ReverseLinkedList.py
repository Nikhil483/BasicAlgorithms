from BasicLinkedListOperations.BasicLinkedListOperation import LinkedList


def reverse_linked_list(l_list):
    left = None
    current = l_list.head

    while current is not None:
        right = current.next # preserves current's next node
        current.next = left # reverses the connection to next node

        # moves the pointer ahead
        left = current
        current = right

    l_list.head = left

if __name__ == "__main__":
    l_list = LinkedList()
    l_list.create_linked_list_from_array([1, 2, 3, 4, 5])
    print("Original list : ", end= "")
    l_list.display()
    print()

    reverse_linked_list(l_list)
    print("reversed list : ", end="")
    l_list.display()