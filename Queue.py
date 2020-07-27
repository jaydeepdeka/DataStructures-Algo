class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def enque(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            ptr = self.first
            self.last.next = node
            self.last = node
        self.length+=1
    def deque(self):
        if self.length == 0:
            return None
        elif self.length==1:
            self.last = None
            this.first = None
        else:
            self.first = self.first.next
        self.length-=1
    def peek(self):
        return self.first
