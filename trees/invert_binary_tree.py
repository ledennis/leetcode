# Given the root of a binary tree, invert the tree, and return its root.
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Thoughts
# Inverting the tree looks like going through each node and swapping the left and right. This can be done iteratively or recursively
# Time is O(n) Space is O(1)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root: TreeNode):
    invert_binary_tree_rec(root)
    return root

def invert_binary_tree_rec(node: TreeNode):
    if node:
        temp_node = node.left
        node.left = node.right
        node.right = temp_node
        invert_binary_tree_rec(node.left)
        invert_binary_tree_rec(node.right)

a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(9)
e = TreeNode(2, a, b)
f = TreeNode(7, c, d)
g = TreeNode(4, e, f)
h = invert_binary_tree(g)