def zigzagLevelOrder(root):
    res=[]
    a=1
    queue=collections.deque()
    queue.append(root)
    while queue:
        m=len(queue)
        level=collections.deque()
        for i in range(m):
            n=queue.popleft()
            if n:
                if a%2:
                    level.append(n.val)
                else:
                    level.appendleft(n.val)
                queue.append(n.left)
                queue.append(n.right)
        if level:
            res.append(level)
        a+=1        
    return res
