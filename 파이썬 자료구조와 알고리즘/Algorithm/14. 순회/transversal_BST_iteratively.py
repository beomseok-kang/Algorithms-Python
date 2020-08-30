from collections import deque
from binary_search_tree import BinarySearchTree, NodeBST

class BSTwithTransversalIterative(BinarySearchTree):
    def inorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                nodes.append(current.value)
                current = current.right
        return nodes
    
    def preorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                nodes.append(current.value)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return nodes

    def preorder2(self):
        nodes = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                nodes.append(current.value)
                stack.append(current.right)
                stack.append(current.left)
        return nodes

    def BFT(self):
        current = self.root
        nodes = []
        queue = deque()
        queue.append(current)
        while queue:
            current = queue.popleft()
            nodes.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return nodes

