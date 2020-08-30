from binary_tree import BinaryTree, NodeBT

class NodeBST(NodeBT):
    def __init__(self, value=None, level=1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None

    def _add_next_node(self, value, level_here=2):
        new_node = NodeBST(value, level_here)
        if value > self.value:
            self.right = self.right and self.right._add_next_node(value, level_here+1) or new_node
        elif value < self.value:
            self.left = self.left and self.left._add_next_node(value, level_here+1) or new_node
        else:
            print("중복 노드를 허용하지 않습니다.")
        return self
    
    def _search_for_node(self, value):
        if self.value == value:
            return self
        elif self.left and value < self.value:
            return self.left._search_for_node(value)
        elif self.right and value > self.value:
            return self.right._search_for_node(value)
        else:
            return False
    
class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None
    
    def add_node(self, value):
        if not self.root:
            self.root = NodeBST(value)
        else:
            self.root._add_next_node(value)