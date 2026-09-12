class Solution(object):
    def climbStairs(self, n):
        if n==1 or n==2:
            return n

        prev1=1
        prev2=2
 
        for i in range(3,n+1):
            curr=prev1+prev2
            prev1=prev2
            prev2=curr

        return prev2

        # return dp[n]
        