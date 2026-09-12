class Solution(object):
    def solve(self,n,dp):
        if n==1 or n==2:
            return n

        if dp[n]!=-1:
            return dp[n]

        dp[n]=self.solve(n-1,dp) + self.solve(n-2,dp)
        return dp[n]

    def climbStairs(self, n):
        dp=[-1]*(n+1)#1D DP 

        return self.solve(n,dp)
        