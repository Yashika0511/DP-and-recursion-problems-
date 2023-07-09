# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(root,res):
    res=[]
    queue=collections.deque()
    queue.append(root)
    while queue:
        m=len(queue)
        level=[]
        for i in range(m):
            n=queue.popleft()
            if n:
                level.append(n.val)
                queue.append(n.left)
                queue.append(n.right)
        if level:
            res.append(level)
    return res
