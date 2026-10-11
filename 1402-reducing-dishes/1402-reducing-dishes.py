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
        dp=[[-1 for _ in range(n+1)]for _ in range(n+1)]
        #Sort the Array
        satisfaction.sort()
        
        # Base case: dp[n][time] = 0 is already handled by initializing with 0
        for time in range(n+1):
            dp[n][time]=0

        for i in range(n-1,-1,-1):
            for time in range(i+1):#the count of disces you already coocked
                include=satisfaction[i]*(time+1) + dp[i+1][time+1]
                exclude=0+ dp[i+1][time]#Time wahi rahega na ager hum dish prepare hi nhi karenga to
                dp[i][time]=max(include,exclude)  

        return dp[0][0]

        