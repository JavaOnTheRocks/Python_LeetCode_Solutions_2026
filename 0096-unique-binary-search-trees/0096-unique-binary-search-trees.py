class Solution(object):
    def Solve(self,n,dp):
        #Base Case
        if n<=1:
            return 1
        
        if dp[n] != -1:
            return dp[n]
        ans=0
        for i in range(1,n+1):
            ans+=self.Solve(i-1,dp)*self.Solve(n-i,dp)
        dp[n]=ans
        return dp[n]

    def numTrees(self, n):
        dp=[-1 for _ in range(n+1)]
        return self.Solve(n,dp)

## Memoization appraoch:

## Time Cmplexity - Exponential - O(n^2)
## Sapce Complexity - O(n) + O(n)
        
        