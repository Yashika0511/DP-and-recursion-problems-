# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

res=[]
def postorderTraversal(root,res):
    if root:
        postorderTaversal(root.left)
        postorderTraversal(root.right)
        res.append(root.val)
print(res)
