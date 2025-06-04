from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# to Collect leaves
# def get_leaves(node, leaves):
#     if not node:
#         return
#     if not node.left and not node.right:
#         leaves.append(node.val)
#     get_leaves(node.left, leaves)
#     get_leaves(node.right, leaves)

# Check Leaf Node

def leafSimilar(root1, root2):
    def get_leaves(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        left = get_leaves(node.left)
        right = get_leaves(node.right)
        combin = left + right
        print(combin)
        return combin

    return get_leaves(root1) == get_leaves(root2)

def maxDef(root):
    if not root:
        return None
    left = maxDef(root.left)
    right = maxDef(root.right)

    return 1+ max(left, right)

# Test input: LeetCode format
root1 = [1,2,3]
root2 = [1,3,2]
tree1 = build_tree_level_order(root1)
tree2 = build_tree_level_order(root2)

print(leafSimilar(tree1, tree2))