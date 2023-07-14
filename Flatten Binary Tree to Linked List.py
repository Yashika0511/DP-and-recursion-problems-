def flatten(root):
        self.head = None
        def revPreOrder(node):
            if node.right: revPreOrder(node.right)
            if node.left: revPreOrder(node.left)
            node.left, node.right, self.head = None, self.head, node
        if root: revPreOrder(root)
