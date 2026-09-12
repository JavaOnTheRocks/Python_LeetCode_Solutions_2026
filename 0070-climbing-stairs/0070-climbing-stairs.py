class Solution(object):
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
            
        dp=[-1]*(n+1)
        
        #tabulization base case 
        dp[1]=1
        dp[2]=2
        # counting the all dp array values 
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]

        # dp=[-1]*(n+1)#1D DP 
        # return self.solve(n,dp)
        