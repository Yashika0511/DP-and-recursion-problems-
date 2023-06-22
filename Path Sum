"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.

A leaf is a node with no children."""\

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def hasPathSum(root, targetSum):
    sum = 0
    return rootToLeafPathSum(root, targetSum, sum)

def rootToLeafPathSum(root, targetSum, sum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        sum += root.val
        if sum == targetSum:
            return True   
    return rootToLeafPathSum(root.left, targetSum, sum + root.val) or rootToLeafPathSum(root.right, targetSum, sum + root.val)
