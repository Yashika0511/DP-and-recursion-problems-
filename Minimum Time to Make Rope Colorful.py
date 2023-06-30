"""Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the
ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of thesame color, so she asks Bob
for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer 
array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful."""

def minCost(s, cost):
        res = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return res
