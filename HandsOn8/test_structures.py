import unittest
from stack import Stack
from myQueue import Queue
from singleLinkedList import SinglyLinkedList

class TestDataStructures(unittest.TestCase):

    ## STACK TESTS ##
    def test_stack(self):
        print("\nTesting Stack...")
        stack = Stack(3)
        
        # Test empty stack behavior
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()
        
        # Push elements
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertTrue(stack.is_full())
        with self.assertRaises(OverflowError):
            stack.push(4)
        
        # Pop elements
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()

    ## QUEUE TESTS ##
    def test_queue(self):
        print("\nTesting Queue...")
        queue = Queue(3)

        # Test empty queue behavior
        self.assertTrue(queue.is_empty())
        with self.assertRaises(IndexError):
            queue.dequeue()
        
        # Enqueue elements
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertTrue(queue.is_full())
        with self.assertRaises(OverflowError):
            queue.enqueue(4)

        # Dequeue elements
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

        self.assertTrue(queue.is_empty())
        with self.assertRaises(IndexError):
            queue.dequeue()

    ## LINKED LIST TESTS ##
    def test_linked_list(self):
        print("\nTesting Singly Linked List...")
        linked_list = SinglyLinkedList(3)

        # Insert elements
        linked_list.insert(10)
        linked_list.insert(20)
        linked_list.insert(30)
        
        self.assertEqual(linked_list.display(), [10, 20, 30])
        
        # Test overflow
        with self.assertRaises(OverflowError):
            linked_list.insert(40)
        
        # Search for elements
        self.assertIsNotNone(linked_list.search(20))
        self.assertIsNone(linked_list.search(99))  # Not in list

        # Delete elements
        linked_list.delete(20)
        self.assertEqual(linked_list.display(), [10, 30])

        linked_list.delete(10)
        self.assertEqual(linked_list.display(), [30])

        linked_list.delete(30)
        self.assertEqual(linked_list.display(), [])

        # Deleting non-existent element
        with self.assertRaises(ValueError):
            linked_list.delete(99)

if __name__ == '__main__':
    unittest.main()
