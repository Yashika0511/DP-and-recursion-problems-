def widthOfBinaryTree(root):
    queue= collections.deque()
    queue.append((root,0))
    maxw = 0
    while queue:
        qlen = len(queue)
        nl,base = queue[0]
        for i in range(qlen):
            node,indx = queue.popleft()
            if node.left:
                queue.append((node.left,2*indx))
            if node.right:
                queue.append((node.right,(2*indx)+1))
            maxw = max(maxw,indx-base+1)
    return maxw
