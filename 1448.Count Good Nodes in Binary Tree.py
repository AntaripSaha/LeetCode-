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

def goodNodes(root):
    def dfs(node, maxSoFar):
        count = 0
        if not node:
            return 0
        if node.val >= maxSoFar:
            count += 1
        updatedMax = max(maxSoFar, node.val)
        count += dfs(node.left, updatedMax)
        count += dfs(node.right, updatedMax)
        return count
    return dfs(root, float("-inf"))




#
# Test input: LeetCode format
values = [3,1,4,3,None,1,5]

# Build tree from input
tree_root = build_tree_level_order(values)

# Call depth function
depth = goodNodes(tree_root)
print("Good Nodes =", depth)  # Expected Output: 3
