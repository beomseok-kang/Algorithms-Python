from transversal_BST_recursive import BSTwithTransversalRecursive

def find_common_ancestor(path, low_value, high_value):
    while path:
        current_value = path[0]
        if current_value < low_value:
            try:
                path = path[2:]
            except:
                return current_value
        elif current_value > high_value:
            try:
                path = path[1:]
            except:
                return current_value
        elif low_value <= current_value <= high_value:
            return current_value

bst = BSTwithTransversalRecursive()
l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
for i in l:
    bst.add_node(i)

path = bst.preorder()
print("전위 순회: ", path)

print("1과 6의 최소 공통 조상: ", find_common_ancestor(path, 1, 6))