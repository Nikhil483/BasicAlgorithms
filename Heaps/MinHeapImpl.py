# this is min heap implementation
# For max heap, we just need to change comparison logic between nodes, that is pointed in code below


class MinHeap :

    def __init__(self):
        self.heap = []

    def getLeftChildIndex(self, parent_index):
        return 2 * parent_index + 1

    def getRightChildIndex(self, parent_index):
        return 2 * parent_index + 2

    def getParentIndex(self, child_index):
        return (child_index - 1) // 2

    def getMin(self):
        if self.getLen() == 0:
            raise IndexError("No elements left to pop")
        return self.heap[0]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def getLen(self):
        return len(self.heap)

    # used to insert values into the heap
    def heapify_up(self, index):
        while index > 0 :
            parent = self.getParentIndex(index)
            if self.heap[index] < self.heap[parent] : # for max heap sign will be '>'
                self.swap(index, parent)
                index = parent
            else :
                break

    def heapify_down(self, index):
        size = self.getLen()
        while True:
            left = self.getLeftChildIndex(index)
            right = self.getRightChildIndex(index)
            smallest = index # this variable can be names largest in max heap for convenience

            if left < size and self.heap[smallest] > self.heap[left] : # for max heap sign will be '>'
                smallest = left
            if right < size and self.heap[smallest] > self.heap[right] : # for max heap sign will be '>'
                smallest = right

            # this check tells if current element is already less than or equal(opposite for max heap) to child nodes
            # in that case we don't need to swap, and tree will be balanced down from there
            if smallest == index:
                break

            self.swap(index, smallest)
            index = smallest


    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(self.getLen() - 1)

    def extract_min(self):
        if self.getLen() == 0:
            raise IndexError("No elements left to pop")
        elif self.getLen() == 1 :
            return self.heap.pop()

        # keep track of what to return
        root = self.heap[0]
        # move last element place of root
        self.heap[0] = self.heap.pop()
        # balance the heap now from top down
        self.heapify_down(0)

        return root



if __name__ == "__main__":
    mh = MinHeap()
    mh.insert(5)
    mh.insert(-5)
    mh.insert(1)
    mh.insert(-3)
    mh.insert(0)
    mh.insert(4)

    print("Heap : " + str(mh.heap))

    print("Min at this point" + str(mh.extract_min()))

    print("Heap : " + str(mh.heap))

    mh.insert(2)

    print("Heap : " + str(mh.heap))

    print("Min at this point" + str(mh.extract_min()))

    print("Min at this point" + str(mh.extract_min()))

    print("Min at this point" + str(mh.extract_min()))

