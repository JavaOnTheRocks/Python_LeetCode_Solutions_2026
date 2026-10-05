class Solution(object):
    def numSquares(self, n):
        dp=[float("inf")]*(n+1) #yaha min squares wala hi store karega
        #Use Base case
        dp[0]=0
        #Recursive Case
        for i in range(1,n+1):
            j=1
            while j*j<=i:
                dp[i]=min(dp[i],1+dp[i-j*j])
                j+=1
        return dp[n]