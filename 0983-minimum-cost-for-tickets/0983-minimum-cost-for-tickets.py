class Solution(object):
    def Solve(self,days,costs,n,index,dp):
        ## Base Case
        if index>=n:
            return 0
            
        if dp[index] != float("inf"):
            return dp[index]
        ## Recursive Case
        #1 day ticket
        option1=costs[0]+self.Solve(days,costs,n,index+1,dp)

        ## 7 Day
        i=index
        while i<n and days[i]<days[index]+7:
            i+=1
            option2=costs[1]+self.Solve(days,costs,n,i,dp)#jesa hi brack hoda 7 day wali cost count karka fir index new milegi usk liya recursive call maar denga

        i=index
        while i<n and days[i]<days[index]+30:
            i+=1
            option3=costs[2]+self.Solve(days,costs,n,i,dp)#jesa hi brack hoda 30 day wali cost count karka fir index new milegi usk liya recursive call maar denga
        
        dp[index]=min (option1,option2,option3)
        return dp[index]

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

## Time Complexity - O(N) becaius we are only computng singel time each and every problem 
## Space Complexity - O(N)+O(N)#Recrisive stacka and the dp aray