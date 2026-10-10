import sys
sys.setrecursionlimit(1000000)
class Solution(object):
    def minSideJumps(self, obstacles):
        n=len(obstacles)-1
        #initallize dp arraay-
        dp=[[ -1 for _ in range(len(obstacles))] for _ in range(4)]

        #Base case
        for lane in range(4):
            dp[lane][n]=0

        #bottom up appraocah 
        for currposition in range(n-1,-1,-1):
            for currlane in range(1,4):
                if obstacles[currposition+1] != currlane:
                    dp[currlane][currposition]=dp[currlane][currposition+1]#Aaga wal copy ker lunga ager sidha move kiya ha to
                else:
                    ans=float("inf")
                    for i in range(1,4):
                        if obstacles[currposition] != i and currlane != i:
                            jump= 1 + dp[i][currposition+1]#bubber wal example ki ager wo abi tuk calculate hi nhi huva ha to 
                            ans=min(ans,jump)
                    dp[currlane][currposition]=ans
        # return dp[2][0]
        return min(dp[2][0],dp[1][0]+1,dp[3][0]+1)