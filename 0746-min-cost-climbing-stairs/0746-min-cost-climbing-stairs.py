class Solution(object):
    def solve(self,n,cost,dp):
        if n==0 or n==1:
            return 0

        dp[0]=0
        dp[1]=0

        if dp[n]!=-1:
            return dp[n]

        for i in range(2,n+1):
            one_step_cost=dp[i-1]+cost[i-1]
            two_step_cost=dp[i-2]+cost[i-2]
            dp[i]=min(one_step_cost,two_step_cost)

        return dp[n]

    def minCostClimbingStairs(self, cost):
        n=len(cost)
        dp=[-1]*(n+1)
        return self.solve(n,cost,dp)



        
        
        