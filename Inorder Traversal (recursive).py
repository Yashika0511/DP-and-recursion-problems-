# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

res=[]
def inorderTraversal(root,res):
    if root:
        inorderTaversal(root.left)
        res.append(root.val)
        inorderTraversal(root.right)
print(res)
