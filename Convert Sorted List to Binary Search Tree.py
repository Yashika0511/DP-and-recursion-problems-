def sortedListToBST(head):
      if not head:
              return None
      if not head.next:
          return TreeNode(head.val)
      slow, fast = head, head.next.next
      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
      root = TreeNode(slow.next.val)
      root.right = self.sortedListToBST(slow.next.next)
      slow.next = None
      root.left = self.sortedListToBST(head)
      return root
