def diameterOfBinaryTree(root):
    self.md=0
    def dia(root):
        if not root:
            return 0

        lh=dia(root.left)
        rh=dia(root.right)

        di= lh+rh
        self.md=max(self.md,di)
        return max(lh,rh)+1
    dia(root)    
    return self.md    
