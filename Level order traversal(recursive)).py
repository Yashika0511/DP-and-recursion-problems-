#level order recursive
def levelOrder(root):
    ans = []
    levels = set()
    def helper(node, level):
        if not node: return

        if level not in levels:
            ans.append([node.val])
            levels.add(level)
        else: 
            ans[level].append(node.val)

        helper(node.left, level+1)
        helper(node.right, level+1)
    helper(root,0)
    return ans
