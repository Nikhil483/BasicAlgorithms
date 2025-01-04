class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


def generate_node(data):
    return Node(data)


class LinkedList :
    def __init__(self):
        self.head = None

    def create_linked_list_from_array(self, args):
        for ele in args :
            self.append(ele)

    # checks if list is empty
    def is_empty(self):
        if self.head is None :
            return True
        return False

    # display the list
    def display(self):
        if self.is_empty():
            print("List does not contain any elements")
            return

        current = self.head
        while current.next :
            print(current.data, end = " => ")
            current = current.next
        print(current.data)

    # check if a value exist in the list
    def search(self, value):
        current = self.head
        while current :
            if current.data == value :
                return True
            current = current.next
        return False

    # add an element at the end
    def append(self, data):
        node = generate_node(data)

        if self.is_empty():
            self.head = node
            return

        last = self.head
        while last.next :
            last  = last.next
        last.next = node

    # add an element at the beginning
    def prepend(self, data):
        node = generate_node(data)
        if self.is_empty() :
            self.head = node
            return

        node.next = self.head
        self.head = node

    # add an element after given values
    def insert_after(self, data, node_value):
        node = generate_node(data)
        current = self.head
        while current:
            if current.data == node_value:
                required_node = current
                node.next = required_node.next
                required_node.next = node
                return True
            current = current.next
        return False

    # add an element after given number of nodes
    def insert_after_count(self, data, count):
        if count == 0 :
            self.prepend(data)
            return True
        node = generate_node(data)
        current = self.head
        count -= 1
        while count > 0 :
            if current.next is None:
                return False
            current = current.next
            count -= 1
        node.next = current.next
        current.next = node
        return True

    # remove an element at the end
    # remove an element at the beginning
    # remove an element/s after given values
    # remove an element after given number of nodes

    # update element/s with given values
    # update element after certain number of nodes


if __name__ == "__main__" :
    list_1 = LinkedList()

    list_2 = LinkedList()
    list_2.create_linked_list_from_array([1, 2, 3, 4, 5])

    print("Print the list 2")
    list_2.display()

    print("Print the list")
    list_1.display()

    print("appending 1, 2, 3")
    list_1.append(1)
    list_1.append(2)
    list_1.append(3)

    print("Print the list")
    list_1.display()

    print("Adding 0 to the front")
    list_1.prepend(0)

    print("Print the list")
    list_1.display()

    print("inserting 2.3  after 2")
    if not list_1.insert_after(2.3, 2) :
        print("Insertion failed")

    print("inserting 0.6  after 0")
    if not list_1.insert_after(0.6, 0) :
        print("Insertion failed")

    print("inserting 7.6  after 7")
    if not list_1.insert_after(7.6, 7) :
        print("Insertion failed")

    print("Print the list")
    list_1.display()

    print("inserting 10  after 2 positions")
    if not list_1.insert_after_count(10, 2):
        print("Insertion failed")

    print("Print the list")
    list_1.display()

    print("inserting -1  after 0 positions")
    if not list_1.insert_after_count(-1, 0):
        print("Insertion failed")

    print("Print the list")
    list_1.display()

    print("inserting 1000  after 20 positions")
    if not list_1.insert_after_count(1000, 8):
        print("Insertion failed")

    print("Print the list")
    list_1.display()