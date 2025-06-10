from collections import deque

from Triplet import count


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_level_order(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root
def print_tree_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # পেছনের null গুলা বাদ দাও
    while result and result[-1] is None:
        result.pop()

    return result

def invertTree(root):
    if not root:
        return None
    # tmp = root.left
    # root.left = root.right
    # root.right = tmp

    root.right, root.left = root.left, root.right

    invertTree(root.left)
    invertTree(root.right)
    return root



#
# Test input: LeetCode format
values = [1,2,3,4,5,6,7]

# Build tree from input
tree_root = build_tree_level_order(values)

# Call depth function
inverted = invertTree(tree_root)
print("Inverted Tree:", print_tree_level_order(inverted)) # Expected Output: 3
