class Node(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    first = None
    last = None
    length = 0

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def append(self, data):  # to the end
        _new_node = Node(data, self.last, None)
        if(self.length == 0):
            self.length += 1
            self.last = _new_node
            self.first = _new_node
            return
        if(self.first is not None):
            self.first.next = _new_node
        else:
            self.last = self.last = _new_node
        self.last = _new_node
        self.length += 1

    def push(self, data):  # to the beg
        _new_node = Node(data, None, self.first)
        if (self.length == 0):
            self.length += 1
            self.last = _new_node
            self.first = _new_node
            return
        if (self.first is not None):
            self.first.prev = _new_node
        else:
            self.last = self.last = _new_node
        self.first = _new_node
        self.length += 1

    def get_last(self):
        return self.last

    def get_first(self):
        return self.first

    def del_last(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.last = None
            self.first = None
            self.length = 0
            return
        tmp = self.last
        self.last = self.last.prev
        del tmp
        if self.last is not None:
            self.last.next = None
        self.length -= 1

    def del_first(self):
        if self.length == 0:
            return
        if (self.length == 1):
            self.last = None
            self.first = None
            self.length = 0
            return
        tmp = self.first
        self.first = self.first.next
        del tmp
        if self.last is not None:
            self.last.next = None
        self.length -= 1

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
