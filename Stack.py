class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        node=Node(value)
        if self.length == 0:
            self.top = node
            self.bottom = node
        else:
            ptr = self.top
            self.top = node
            self.top.next = ptr
        self.length+=1
    def pop(self):
        if self.length==0:
            print("Empty Stack")
            return
        else:
            self.top = self.top.next
            self.length-=1
    def peek(self):
        return self.top
    def __repr__(self):
        ptr = self.bottom
        while ptr.next!=None:
            print(ptr.value)
            ptr=ptr.next
