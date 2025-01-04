from BasicLinkedListOperations.BasicLinkedListOperation import Node

def print_list(head):
    count = 7 # stops infinite loop to see cycle
    current = head
    while current.next  and count > 0 :
        count -= 1
        print(current.data, end = " => ")
        current = current.next
    print(current.data)

def detect_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast : # loops detected here
            slow = head # slow or fast needs to set to head and moved slowly, the pointer meets the cycle starting point

            while slow != fast :
                slow = slow.next
                fast = fast.next

            return slow
    return False


if __name__ == "__main__" :
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    head.next.next.next.next.next.next = head.next
    print_list(head)

    node = detect_loop(head)

    if node :
        print(f"Loop starts at node {node.data}")
    else :
        print("No cycles detected in the list")