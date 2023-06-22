def binStr_helper(arr,num,n):
    if(r == num):
        for i in range(num):
            print(arr[i],end="")
        print(end=" ")
        return
     
    elif(arr[n-1]):
        arr[n] = 0
        binStr(arr, num, n + 1)
    else:
        arr[n] = 0
        binStr(arr,num,n+1)
        arr[n] = 1
        binStr(arr,num,n+1)
 
 
def binStr(a,num):
    a[0] = 0
    binStr(a,num,1)
    a[0] = 1
    binStr(a,num,1)
