"""Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sumOfLeftLeaves(root):
    sum = 0
    def function(root,x, sum):
        if not root.left and not root.right:
            if x == 'left':
                sum += root.val
        if root.left:
            function(root.left, "left", sum)
        if root.right:
            function(root.right, "right", sum)

    function(root, "")
    return sum
