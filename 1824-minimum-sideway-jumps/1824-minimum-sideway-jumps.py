import sys
sys.setrecursionlimit(1000000)
class Solution(object):
    def Solve(self,obstacles,currlane,currposition,dp):
        n=len(obstacles)-1
        #Base Case
        if currposition==n:
            return 0
        
        #if ans already exist then return the ans
        if dp[currlane][currposition] != -1:
            return dp[currlane][currposition]
        #Recursive Case(ak ma solve karunga baaki recursion laka dega)

        #Continue Moving Forward
        if obstacles[currposition+1] != currlane:
            ans=self.Solve(obstacles,currlane,currposition+1,dp)#Jump 0
        else:
            ans=float("inf")
            for i in range(1,4):
                if obstacles[currposition] != i and currlane != i:
                    jump= 1 + self.Solve(obstacles,i,currposition,dp)
                    ans=min(ans,jump)

        dp[currlane][currposition]=ans
        return dp[currlane][currposition]          

    def minSideJumps(self, obstacles):
        #initallize dp arraay-
        dp=[[ -1 for _ in range(len(obstacles))] for _ in range(4)]
        return self.Solve(obstacles,2,0,dp)