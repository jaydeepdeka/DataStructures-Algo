from Trees import BSTree

class BSTree(BSTree):
    def __init__(self):
        super().__init__()
    def bfs(self):
        ptr = self.root
        lst = []
        queue = []
        queue.append(ptr)
        while len(queue)>0:
            temp_ptr = queue.pop(0)
            if temp_ptr.left:
                queue.append(temp_ptr.left)
            if temp_ptr.right:
                queue.append(temp_ptr.right)
            lst.append(temp_ptr.value)
        return lst

    def bfsRecursive(self, queue, lst):
        if not len(queue):
            return lst
        temp_ptr = queue.pop(0)
        if temp_ptr.left:
           queue.append(temp_ptr.left)
        if temp_ptr.right:
           queue.append(temp_ptr.right)
        lst.append(temp_ptr.value)        
        return self.bfsRecursive(queue, lst)

    def dfsIn(self):
        return self.traverseInOrder(self.root, [])
    
    def dfsPre(self):
        return self.traversePreOrder(self.root, [])
    
    def dfsPost(self):
        return self.traversePostOrder(self.root, [])
    
    def traverseInOrder(self, node, lst):
        if (node.left):
            self.traverseInOrder(node.left, lst)
        lst.append(node.value)
        if (node.right):
            self.traverseInOrder(node.right, lst)
        return lst
    
    def traversePreOrder(self, node, lst):
        lst.append(node.value)
        if (node.left):
            self.traversePreOrder(node.left, lst)
        if (node.right):
            self.traversePreOrder(node.right, lst)
        return lst
    
    def traversePostOrder(self, node, lst):
        lst.append(node.value)
        if (node.left):
            self.traversePostOrder(node.left, lst)
        if (node.right):
            self.traversePostOrder(node.right, lst)
        lst.append(node.value)
        return lst
