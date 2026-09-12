class Solution(object):
    def solve(self,n,cost,dp):
        if n==0 or n==1:
            return 0

        if dp[n]!=-1:
            return dp[n]

        one_step_cost=self.solve(n-1,cost,dp)+cost[n-1]
        two_step_cost=self.solve(n-2,cost,dp)+cost[n-2]
        
        #Store Result inside dp
        dp[n]=min(one_step_cost,two_step_cost)
        return dp[n]

    def minCostClimbingStairs(self, cost):
        n=len(cost)
        dp=[-1]*(n+1)
        return self.solve(n,cost,dp)



        
        
        