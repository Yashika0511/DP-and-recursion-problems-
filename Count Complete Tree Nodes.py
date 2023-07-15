def countNodes(root):
    def travel(tree):
        if tree:
            return 1+travel(tree.left)+travel(tree.right)
        return 0
    
    return travel(root)
