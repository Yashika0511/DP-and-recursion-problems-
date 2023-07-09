def isCompleteTree(root):
    if not root:
        return
    q=[root]
    while(q[0]):
        node=q.pop(0)
        q.append(node.left)
        q.append(node.right)
    return not any(q)
