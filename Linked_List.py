class Node():
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

class LinkedList():
    def __init__(self, val):
        node = Node(val)
        self.headval = node
        self.length = 0
        self.tail = self.headval
    def append(self, value):
        node = Node(value)
        self.tail.nxt = node
        self.tail = node
        self.length +=1
        return
    def prepend(self, value):
        node = Node(value)
        node.nxt = self.headval
        self.headval = node
        self.length+=1
        return
    def __repr__(self):
        ptr = self.headval
        while ptr!=self.tail:
            node = ptr
            print(f"{ptr.value}-->")
            ptr = ptr.nxt
        print(f"{self.tail.value}")
        return
    def insert(self, index, value):
        if index>self.length:
            print("Index more than length")
            return None
        ptr = self.traverse(index)
        node = Node(value)
        node.nxt = ptr.nxt
        ptr.nxt = node
        self.length+=1
        return
    def traverse(self, index):
        count = 1
        ptr = self.headval
        while count<index:
            ptr = ptr.nxt
            count+=1
        return ptr
    def remove(self, index):
        if index>self.length:
            print("Index more than length")
            return None           
        ptr = self.traverse(index-1)
        ptr.nxt = ptr.nxt.nxt
        self.length-=1
        return

class DoubleNode():
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.nxt = nxt
        self.prev = prev
class DoublyLinkedList():
    def __init__(self, val):
        node = Node(val)
        self.headval = node
        self.length = 0
        self.tail = self.headval
    def append(self, value):
        node = DoubleNode(value)
        self.tail.nxt = node
        node.prev = self.tail
        self.tail = node
        self.length +=1
    def prepend(self, value):
        node = DoubleNode(value)
        node.nxt = self.headval
        self.headval = node
        self.length+=1
        return
    def insert(self, index, value):
        if index>self.length:
            print("Index more than length")
            return None
        ptr = self.traverse(index)
        node = Node(value)
        node.prev = ptr
        node.nxt = ptr.nxt
        ptr.nxt.prev = node
        ptr.nxt = node
        self.length+=1
        return
    def remove(self, index):
        if index>self.length:
            print("Index more than length")
            return None           
        ptr = self.traverse(index-1)
        ptr.nxt.nxt.prev = ptr
        ptr.nxt = ptr.nxt.nxt
        self.length-=1
        return
    def __repr__(self):
        ptr = self.headval
        while ptr!=self.tail:
            node = ptr
            print(f"{ptr.value}-->")
            ptr = ptr.nxt
        print(f"{self.tail.value}")
        return
    def traverse(self, index):
        count = 1
        ptr = self.headval
        while count<index:
            ptr = ptr.nxt
            count+=1
        return ptr
