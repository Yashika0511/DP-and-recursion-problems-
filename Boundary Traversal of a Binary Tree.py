def printLeaves(root):
    if(root):
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.data)
        printLeaves(root.right)

def printBoundaryLeft(root):
    if(root):
        if (root.left):
            print(root.data)
            printBoundaryLeft(root.left)
         
        elif(root.right):
            print (root.data)
            printBoundaryLeft(root.right)
  
def printBoundaryRight(root):
     
    if(root):
        if (root.right):
            printBoundaryRight(root.right)
            print(root.data)
         
        elif(root.left):
            printBoundaryRight(root.left)
            print(root.data)
  
def printBoundary(root):
    if (root):
        print(root.data)
        printBoundaryLeft(root.left)

        printLeaves(root.left)
        printLeaves(root.right)
 
        printBoundaryRight(root.right)
