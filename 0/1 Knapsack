#0/1 Knapsack

"""A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items. Its weight is given
by the ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but 
can’t partially have it as a fraction. We need to find the maximum value of items that the thief can steal."""

def knapsack(w,val,wt):
    n=len(val)
    dp=[[0 for j in range(w+1)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        for j in range(0,w):
            if wt[i]<= w:
                ans=max(val[i]+ dp[i+1][w-wt[i]], dp[i+1][w])
            else:
                ans=dp[i+1][w]
            dp[i][w]=ans
    return dp[0][w]              
