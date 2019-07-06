class Node():
    def __init__(self,data):
        self.val = data
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        # if self.tail is None:
        #     self.tail = node
        #     self.head = Node
        # else:
        #     current = self.tail
        #     while current.next:
        #         current = current.next
        #     current.next = node
        
        if  self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    """ Traversing through linked List to find its size """
    def get_list_size(self):
        current = self.tail
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def iter(self):
        current = self.tail
        while current:
            val = current.val
            current = current.next
            yield val
   
    # delete a node
    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.val == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
            
            prev = current
            current = current.next

    # search
    def search(self, data):
        current = self.tail
        while current:
            if current.val == data:
                return 'Found'
            current = current.next
        return 'Not Found'

    # clear linked list
    def clear(self):
        self.head = None
        self.tail = None

if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.append('Pizza')
    ll.append('Burger')
    ll.append('Curry')
    ll.append('Pasta')
    print('Get Size of the List {}'.format(ll.get_list_size()))
    print('Get Size of the List {}'.format(ll.size))
   
    def prt():
        for val in ll.iter():
            print(val, end = " => ")
        print()
    prt()
    ll.delete('Pasta')

    print(ll.search('Pasta'))
    ll.clear()
    prt()