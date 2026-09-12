class Solution(object):
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        dp=[-1]*(n+1)

        if n==0 or n==1:
            return 0

        prev2=0
        prev1=0

        for i in range(2,n+1):
            one_step_curr = prev1 + cost[i-1]
            two_step_curr = prev2 + cost[i-2]
            curr=min(one_step_curr,two_step_curr)
            prev2=prev1
            prev1=curr

        return prev1



        
        
        