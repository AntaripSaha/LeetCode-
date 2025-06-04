from collections import deque

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

def maxDepth(root):
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    print("left: ",left)
    # print("right: ",right)

    return 1 + max(left, right)



# Test input: LeetCode format
values = [3, 9, 20, None, None, 15, 7]

# Build tree from input
tree_root = build_tree_level_order(values)

# Call depth function
depth = maxDepth(tree_root)
print("Maximum Depth =", depth)  # Expected Output: 3
