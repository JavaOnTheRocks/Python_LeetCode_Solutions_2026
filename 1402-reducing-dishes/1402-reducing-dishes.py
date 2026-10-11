class Solution(object):
    def Solve(self,satisfaction,index,time,dp):
        #Base Case
        if index>=len(satisfaction):
            return 0
        if dp[index][time] != -1:
            return dp[index][time]
        #Recursive Case
        include=satisfaction[index]*(time+1) + self.Solve(satisfaction,index+1,time+1,dp)
        exclude=0+self.Solve(satisfaction,index+1,time,dp)#Time wahi rahega na ager hum dish prepare hi nhi karenga to
        dp[index][time]=max(include,exclude)
        return dp[index][time]

    def maxSatisfaction(self, satisfaction):
        n=len(satisfaction)
        dp=[[-1 for _ in range(n)]for _ in range(n)]
        #Sort the Array
        satisfaction.sort()
        return self.Solve(satisfaction,0,0,dp)

        