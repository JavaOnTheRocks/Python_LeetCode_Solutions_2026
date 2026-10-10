import sys
sys.setrecursionlimit(1000000)
class Solution(object):
    def minSideJumps(self, obstacles):
        n=len(obstacles)-1
        #initallize dp arraay-
        curr=[ float("inf") for _ in range(4)]
        next=[float("inf") for _ in range(4)]


        #Base case
        next[0]=0
        next[1]=0
        next[2]=0
        next[3]=0

        #bottom up appraocah 
        for currposition in range(n-1,-1,-1):
            for currlane in range(1,4):
                if obstacles[currposition+1] != currlane:
                    curr[currlane]=next[currlane]#Aaga wal copy ker lunga ager sidha move kiya ha to
                else:
                    ans=float("inf")
                    for i in range(1,4):
                        if obstacles[currposition] != i and currlane != i:
                            jump= 1 + next[i]#bubber wal example ki ager wo abi tuk calculate hi nhi huva ha to 
                            ans=min(ans,jump)
                    curr[currlane]=ans
            #after each iteration 
            next=curr
        # return dp[2][0]
        return min(next[2],next[1]+1,next[3]+1)