def searchBST(root, val):
        while root!=None and root.val!=val:
            if root.val<val:
                root=root.right
            else:
                root=root.left
        return root
