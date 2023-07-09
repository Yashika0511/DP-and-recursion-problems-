def isSymmetric(root):
    def check_sym(left_subtree, right_subtree):
        if left_subtree and right_subtree:
            return left_subtree.val == right_subtree.val and check_sym(left_subtree.left, right_subtree.right) and check_sym(left_subtree.right, right_subtree.left)
        return left_subtree == right_subtree

    return check_sym(root.left, root.right)
