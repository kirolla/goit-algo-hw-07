class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def calculate_tree_sum(root):
    if root is None:
        return 0
    
    # Рекурсивно обчислюємо суму лівого та правого піддерев
    left_sum = calculate_tree_sum(root.left)
    right_sum = calculate_tree_sum(root.right)
    
    # Повертаємо суму значень поточного вузла та суми піддерев
    return root.val + left_sum + right_sum

# Приклад використання:
# Створення AVL-дерева
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

# Знаходження суми всіх значень в дереві
tree_sum = calculate_tree_sum(root)
print("Сума всіх значень в AVL-дереві:", tree_sum)
