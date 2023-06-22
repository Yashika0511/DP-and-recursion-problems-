"""Given an array of integers, print a sum triangle from it such that the first level has all array elements. 
From then, at each level number of elements is one less than the previous level and elements at the level is be 
the Sum of consecutive two elements in the previous level. """

def Tri(A):
        if (len(A) < 1):
            return
        t = [0] * (len(A) - 1)
        for i in range( 0, len(A) - 1):
           
            x = A[i] + A[i + 1]
            t[i] = x
        Tri(t)
        print(A)
