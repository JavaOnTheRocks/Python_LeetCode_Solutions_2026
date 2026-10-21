class Solution(object):
    def Solve(self,prices,index,Buy,dp):
        if index == len(prices):
            return 0
        
        if dp[Buy][index] != -1:
            return dp[Buy][index]

        profit=0
        #Recursive Approach:(include or Exclude)
        n=len(prices)
        if Buy==1:
            ## Buy
            buykaro=-prices[index]+self.Solve(prices,index+1,0,dp)
            ## Skip
            skip=0+self.Solve(prices,index+1,1,dp)#abhi buy nhi kiya aaga jaka buy kareanga
            profit+=max(buykaro,skip)

        else:
            ## Sell
            sellkaro=prices[index]+self.Solve(prices,index+1,1,dp)
            ## Skip
            skip=0+self.Solve(prices,index+1,0,dp)#abhi sell nhi kiya aaga jaka sell karenga
            profit+=max(sellkaro,skip)
        
        dp[Buy][index]=profit
        return dp[Buy][index]

    def maxProfit(self, prices):
        n=len(prices)
        if not prices:
            return 0

        dp=[[-1 for _ in range(n+1)]for _ in range(2)]#Two variable changing Buy status and the dp 

        return self.Solve(prices,0,1,dp)#pahala Buy karna tabhi to baad ma sell ker paunga

## Time Complexity - O(N) Exponential  TLE
## Space Complexity - O(N) dp Space  + O(N) Recusion stack depth

        

        
        




        