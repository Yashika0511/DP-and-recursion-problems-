"""You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way."""

def maxUncrossedLines(nums1, nums2):
        n,m=len(nums1),len(nums2)
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
