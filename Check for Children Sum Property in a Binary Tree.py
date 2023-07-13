def isSumProperty(node):
    left_data = 0
    right_data = 0
    if(node == None or (node.left == None and
                        node.right == None)):
        return True
    else:
 
        if(node.left != None):
            left_data = node.left.data

        if(node.right != None):
            right_data = node.right.data

        if((node.data == left_data + right_data) and
           isSumProperty(node.left) and
           isSumProperty(node.right)):
            return True
        else:
            return False
