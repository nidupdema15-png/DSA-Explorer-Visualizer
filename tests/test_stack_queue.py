import unittest
from dsa_logic import Stack, Queue


class TestStackQueue(unittest.TestCase):

    def test_stack_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)

    def test_stack_empty_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_queue_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.size(), 1)

    def test_queue_empty_dequeue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())


if __name__ == "__main__":
    unittest.main()
