def minDepth(root):
    def count(root):
        if root is None:
            return 0
        if root.left is None:
            return count(root.right) + 1
        if root.right is None:
            return count(root.left) + 1
        return min(count(root.left), count(root.right)) + 1
    return count(root)
