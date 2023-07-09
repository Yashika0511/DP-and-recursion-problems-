# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root,res):
    stack=[]
    res=[]
    while stack or root:
        if root:
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            res.append(root.val)
            root=root.right
    return res    
