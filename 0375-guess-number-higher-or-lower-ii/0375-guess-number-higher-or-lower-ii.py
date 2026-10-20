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

    def SolveTab(self,start,end):
        n=end
        #make teh range (n+2) do handel teh Boundry Condition
        dp=[[0 for _ in range(n+2)]for _ in range(n+2)]

        #Iterative Approach:
        for start in range(n,-1,-1):
            for end in range(1,n+1):
                if start>= end :
                    continue
                else:
                    ans=float("inf")
                    for num in range(start,end+1):
                        ans=min(ans,num+max(dp[start][num-1],dp[num+1][end]))
                    dp[start][end]=ans

        return dp[start][end]


    def getMoneyAmount(self, n):
        #2D Dp 
        return self.SolveTab(1,n)
    
## Time Complexity - Exponential O(n^3)
## Space Complexity - O(n^2)  .. (No Recursive Depth error occur)


        