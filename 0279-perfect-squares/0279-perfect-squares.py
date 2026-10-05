class Solution(object):
#Now we are calcuatin every problem Single time no recomuptin subproblems 
    def SolveMem(self,n,dp):
        #Base Case
        if n==0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        #Recursive Case
        min_squares=float("inf")
        j=1
        while j*j<=n:
            current_squares=1+self.SolveMem(n-j*j,dp)
            min_squares=min(min_squares,current_squares)
            j+=1
        dp[n]=min_squares
        return dp[n]

    def numSquares(self, n):
        dp=[-1]*(n+1)
        return self.SolveMem(n,dp)
        

        