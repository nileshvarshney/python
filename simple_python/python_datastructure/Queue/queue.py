class Queue():
    def __init__(self):
        self.item = []
        self.size = 0

    def enQueue(self, data):
        self.item.insert(0, data)
        self.size += 1
    
    def deQueue(self):
        data = self.item.pop()
        self.size -= 1
        return data

if __name__ == "__main__":
    q = Queue()
    for i in [10, 20, 30]:
        q.enQueue(i)
    
    for cntr in range(q.size):
        print(q.deQueue(), end=" ")
    print()
