class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class  DoublyLinkedList (object):

    def __init__(self):
        pass

    self.first = None
    self.last = None
    self.length = 0

    def append(self, data):  # to the end
        _new_node = Node(data, self.last, None)
        self.first.next = _new_node
        self.last = _new_node

    def push(self, data):  # to the beg
        _new_node = Node(data, None, self.first)
        self.first.prev = _new_node
        self.first = _new_node

    def get_last(self):
        return self.last

    def get_first(self):
        return self.first

    def del_last(self):
        if self.last is None:
            return
        tmp = self.last
        self.last = self.last.prev
        del tmp
        self.last.next = None

    def del_first(self):
        if self.first is None:
            return
        tmp = self.first
        self.first = self.first.next
        del tmp
        self.last.next = None

    def size(self):
        return self.length

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = '[\n' + current.data + '\n'
            while current.next is not None:
                current = current.next
                out += current.data + '\n'
            return out + ']'
        return '[]'

