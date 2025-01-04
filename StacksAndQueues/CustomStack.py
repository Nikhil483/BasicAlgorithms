class Stack :
    def __init__(self, max_element):
        self.stack = []
        self.num_of_ele = 0
        self.max = max_element

    def push(self, value):
        if self.num_of_ele >= self.max :
            print("Stack is full, try removing some elements")
        else :
            self.stack.append(value)
            self.num_of_ele += 1

    def pop(self):
        if self.num_of_ele <= 0 :
            print("Stack is empty, try adding some values")
        else :
            self.num_of_ele -= 1
            return self.stack.pop()

    def print(self):
        count = self.num_of_ele
        while count > 0 :
            count -= 1
            print(self.stack[count])


if __name__ == "__main__" :
    s = Stack(5)
    s.pop()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.push(4)
    s.push(5)
    s.print()
    s.push(6)