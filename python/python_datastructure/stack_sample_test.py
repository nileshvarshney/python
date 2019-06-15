import unittest

from stack_sample import Stack

class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_first_push(self):
        self.stack.push(10)
        #top = self.stack.peek()
        self.assertEqual(self.stack.peek(),10)

    def test_first_push_count(self):
        self.stack.push(100)
        self.assertEqual(self.stack.count,1)

    def test_multi_push(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        #top = self.stack.peek()
        self.assertEqual(self.stack.peek(),30)

    def test_push_count(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.count,3)

    def test_first_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.pop(),30)

    
    def test_multiple_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.pop(),30)
        self.assertEqual(self.stack.pop(),20)

    
    def test_beyond_last_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.pop(),None)


if __name__ == "__main__":
    unittest.main()
        
