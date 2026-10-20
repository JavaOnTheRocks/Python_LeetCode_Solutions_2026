class Solution(object):
    def Solve(self,start,end):
        if start >= end:
            return 0
        ans=float("inf")
        for num in range(start,end+1):
            ans=min(ans,num+max(self.Solve(start,num-1),self.Solve(num+1,end)))
        return ans

    def SolveMem(self,start,end,dp):
        if start >= end:
            return 0

        if dp[start][end] != -1:
            return dp[start][end]

        ans=float("inf")
        for num in range(start,end+1):
            ans=min(ans,num+max(self.SolveMem(start,num-1,dp),self.SolveMem(num+1,end,dp)))
        dp[start][end]=ans
        return dp[start][end]

    def getMoneyAmount(self, n):
        #2D Dp 
        dp=[[-1 for _ in range(n+1)]for _ in range(n+1)]
        return self.SolveMem(1,n,dp)
    
## Time Complexity - Exponential O(n^2)
## Space Complexity - O(n^2) .. Recursive Stack


        