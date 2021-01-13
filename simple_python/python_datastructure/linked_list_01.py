class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node('Egg')
n2 = Node('Ham')
n3 = Node('Spam')
n4 = Node('Hen')

n1.next = n2
n2.next = n3
n3.next = n4

#  traversing
current = n1
while current:
    print(current.data)
    current = current.next


############################################
# Single Link List
############################################
class SingleLinkList():
    def __init__(self):
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
    def get_size(self):
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count
    
    def iter(self):
        current = self.tail
        while current:
            print(current.data, end = "=>")
            current = current.next
        print()

    def delete(self,data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

n = SingleLinkList()
n.append(10)
n.append(20)
n.append(30)
n.append(40)
n.append(5)
print('Size of Linked List {}'.format(n.get_size()))
n.iter()
n.delete(40)
n.iter()