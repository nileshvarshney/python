class Queue:
    def __init__(self):
        self.s1 =[]
        self.s2=[]
    
    def enQueue(self, x):
        # Move all elements from s1 to s2
        while(len(self.s1) != 0):
            self.s2.append(self.s1[-1])
            self.s1.pop()
       
        """Push item into s1"""
        self.s1.append(x)

        # push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        if len(self.s1) == 0:
            print("Empty Queue")
        else:
            x = self.s1[-1]
            self.s1.pop()
            return x

if __name__ == "__main__":
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())