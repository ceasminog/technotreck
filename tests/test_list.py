import unittest
from _main.py import *


class TestDoublyLinkedList(unittest.TestCase):

    def test_size(self):
        l = DoublyLinkedlist()
        self.assertEqual(l.size(), 0)
        l.append(1)
        self.assertEqual(l.size(), 1)
        l.push(2)
        self.assertEqual(l.size(), 2)
        l.append(3)
        self.assertEqual(l.size(), 3)
        l.push(4)
        self.assertEqual(l.size(), 4)
        
    def test_add_del(self):
        self.assertEqual(l.get_first() is None)
        l = DoublyLinkedlist()
        l.append(1)
        self.assertEqual(l.get_first().data == 1)
        self.assertEqual(l.get_last().data == 1)
        l.push(2)
        self.assertEqual(l.get_first().data == 2)
        self.assertEqual(l.get_last().data == 1)
        l.append(3)
        self.assertEqual(l.get_first().data == 3)
        self.assertEqual(l.get_last().data == 2)


if __name__ == '__main__':
    unittest.main()

