class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
             self.top = node
        self.count += 1
   
    def pop(self):
        if self.top:
            data = self.top.data
            self.count -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top =None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            None

# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.peek())
# print(stack.pop())
# print(stack.pop())
            





