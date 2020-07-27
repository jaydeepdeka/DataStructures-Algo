class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            ptr = self.root
            while True:
                if ptr.value>value:
                    if not ptr.left:
                        ptr.left = node
                        break
                    else:
                        ptr = ptr.left
                else:
                    if not ptr.right:
                        ptr.right = node
                        break
                    else:
                        ptr = ptr.right
    def lookup(self, value):
        ptr = self.root
        level = 0
        found = False
        if ptr.value == value:
            return level
        else:
            ptr = self.root
            while ptr:
                if ptr.value==value:
                    found = True
                    break
                elif ptr.value>value:
                    if ptr.left:
                        ptr = ptr.left
                        level+=1
                elif ptr.value<value:
                    if ptr.right:
                        ptr = ptr.right
                        level+=1
            if found:
                return level, ptr
            else:
                return None
        def remove(self, value):
            if not self.root:
                return None
            else:
                ptr = self.root
                parent = None
                while ptr:
                    if ptr.value == value:
                        break
                    elif ptr.value<value:
                        parent = ptr
                        ptr = ptr.right
                    else:
                        parent = ptr
                        ptr = ptr.left
                if not ptr.right and not ptr.left:
                    if parent.left == value:
                        parent.left = None
                    else:
                        parent.right = None
                elif ptr.left:
                    parent.left = ptr.left
                elif ptr.right.left:
                    parent.right = ptr.right.left
                    
                        
                    
        
