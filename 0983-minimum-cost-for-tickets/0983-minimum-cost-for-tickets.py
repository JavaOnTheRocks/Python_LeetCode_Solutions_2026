class Solution(object):
    def mincostTickets(self, days, costs):
        n=len(days)
        dp=[float("inf")]*(n+1)
        #Base Case 
        dp[n]=0
        #Same Recursive step ko copy karo and recusive call to dp ma convert ker do:
        for k in range(n-1,-1,-1):
            #1 day ticket
            option1=costs[0]+dp[k+1]

            ## 7 Day
            i=k
            while i<n and days[i]<days[k]+7:
                i+=1
                option2=costs[1]+dp[i]#jesa hi brack hoda 7 day wali cost count karka fir index new milegi usk liya recursive call maar denga

            i=k
            while i<n and days[i]<days[k]+30:
                i+=1
                option3=costs[2]+dp[i]#jesa hi brack hoda 30 day wali cost count karka fir index new milegi usk liya recursive call maar denga 

            dp[k]=min(option1,option2,option3)
        return dp[0]

# the space is better than top-down because we completely removed the recursion stack!
## Time Complexity - O(N)
## Space Complexity - O(N) dp array