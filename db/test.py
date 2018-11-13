


'''class Firstclass:



import unittest
from _main import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_size(self):
        new_list = DoublyLinkedList()
        self.assertEqual(new_list.size(), 0)
        new_list.append(1)
        self.assertEqual(new_list.size(), 1)
        new_list.append(1)
        self.assertEqual(new_list.size(), 2)
        new_list.append(1)
        self.assertEqual(new_list.size(), 3)

    def test_add_append(self):
        new_list = DoublyLinkedList()
        self.assertEqual(new_list.get_first(), None)
        self.assertEqual(new_list.get_last(), None)
        new_list.append(1)
        self.assertEqual(new_list.size(), 1)
        self.assertEqual(new_list.get_last().data, 1)
        self.assertEqual(new_list.get_first().data, 1)
        new_list.push(2)
        self.assertEqual(new_list.size(), 2)
        new_list.append(3)
        self.assertEqual(new_list.get_last().data, 3)
        self.assertEqual(new_list.size(), 3)
        new_list.push(4)
        self.assertEqual(new_list.size(), 4)

    def test_del(self):
        new_list = DoublyLinkedList()
        self.assertEqual(new_list.get_first(), None)
        new_list.append(1)
        new_list.push(2)
        new_list.del_last()
        self.assertEqual(new_list.size(), 1)
        new_list.push(2)
        new_list.del_first()
        self.assertEqual(new_list.size(), 1)
        new_list.del_first()
        self.assertEqual(new_list.get_first(), None)
        self.assertEqual(new_list.get_last(), None)
        new_list.push(1)
        new_list.push(2)
        new_list.push(2)
        new_list.del_last()
        self.assertEqual(new_list.size(), 2)
        self.assertEqual(new_list.last.data, 2)

if __name__ == '__main__':
    unittest.main()
'''