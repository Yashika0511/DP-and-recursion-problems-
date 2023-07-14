def deleteNode(root, key):
    if not root: return None
    
    if root.val == key:
        if not root.right: return root.left
        
        if not root.left: return root.right
        
        if root.left and root.right:
            temp = root.right
            while temp.left: temp = temp.left
            root.val = temp.val
            root.right = deleteNode(root.right, root.val)

    elif root.val > key:
        root.left = deleteNode(root.left, key)
    else:
        root.right = deleteNode(root.right, key)
        
    return root
