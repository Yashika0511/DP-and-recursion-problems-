# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def postorderTraversal(root,res):
    res=[]
    queue=collections.deque()
    if root:
        queue.append(root)
    while queue:
        n=queue.popleft()
        res.append(n.val)
        if n.left:
            queue.appendleft(n.left)    
        if n.right:
            queue.appendleft(n.right)
    return res 
