class Solution(object):
    def maxSatisfaction(self, satisfaction):
        n=len(satisfaction)
        curr=[0 for _ in range(n+1)]
        next=[0 for _ in range(n+1)]
        #Sort the Array
        satisfaction.sort()
        
        # Base case: dp[n][time] = 0 is already handled by initializing with 0

        for i in range(n-1,-1,-1):
            for time in range(i+1):#the count of disces you already coocked
                include=satisfaction[i]*(time+1) + next[time+1]
                exclude=0+ next[time]#Time wahi rahega na ager hum dish prepare hi nhi karenga to
                curr[time]=max(include,exclude)  
            next=curr
        return next[0]

## Time Complexity - O(n^2)
## Space Complexity -O(n)