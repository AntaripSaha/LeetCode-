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
    # print("left: ",left)
    # # print("right: ",right)

    return 1 + max(left, right)

# count the total nodes of a tree

def countNodes(root):
    if root == None:
        return 0
    leftCount = countNodes(root.left)
    rightCount = countNodes(root.right)
    return leftCount + rightCount + 1

def sumNodes(root):
    if not root:
        return 0
    leftSum = sumNodes(root.left)
    rightSum = sumNodes(root.right)
    return leftSum + rightSum + root.val

# check the leaf Nodes

def leafSimilar(root1, root2):
    def get_leaves(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return get_leaves(node.left) + get_leaves(node.right)
    return get_leaves(root1) == get_leaves(root2)

#
# # Test input: LeetCode format
# values = [3, 9, 20, None, None, 15, 7]
#
# # Build tree from input
# tree_root = build_tree_level_order(values)
#
# # Call depth function
# depth = maxDepth(tree_root)
# print("Maximum Depth =", depth)  # Expected Output: 3
#
# # Call Count function
# countAll = countNodes(tree_root)
# print("Total Nodes =", countAll)  # Expected Output: 3
# #
# # # Call sum function
# sumAll = sumNodes(tree_root)
# print("Sum of Nodes =", sumAll)  # Expected Output: 3

# Leaf similarity check function
list1 = [3,5,1,6,2,9,8,None,None,7,4]
list2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

root1 = build_tree_level_order(list1)
root2 = build_tree_level_order(list2)
similarLeaf = leafSimilar(root1, root2)
print("Leaves are Same =", similarLeaf)  # Expected Output: 3
