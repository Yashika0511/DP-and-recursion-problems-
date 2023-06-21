"""You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def longestZigZag(root):
        def helper(root, right, total):
            if not root:
                return total
            
            l = helper(root.left, False, total+1 if right else 1)
            r = helper(root.right, True, total+1 if not right else 1)

            return max(l,r)
        
        return helper(root, None, 0) - 1
