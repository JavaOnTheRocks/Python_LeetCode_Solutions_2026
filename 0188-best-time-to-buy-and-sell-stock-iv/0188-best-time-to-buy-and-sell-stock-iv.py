class Solution(object):
    def Solve(self,prices,index,Buy,limit,dp):
        if index == len(prices):
            return 0
            
        if limit == 0:
            return 0
        
        if dp[index][Buy][limit] != -1:
            return dp[index][Buy][limit]

        profit=0
        #Recursive Approach:(include or Exclude)
        n=len(prices)
        if Buy==1:
            ## Buy
            buykaro=-prices[index]+self.Solve(prices,index+1,0,limit,dp)
            ## Skip
            skip=0+self.Solve(prices,index+1,1,limit,dp)#abhi buy nhi kiya aaga jaka buy kareanga
            profit+=max(buykaro,skip)

        else:
            ## Sell
            sellkaro=prices[index]+self.Solve(prices,index+1,1,limit-1,dp)
            ## Skip
            skip=0+self.Solve(prices,index+1,0,limit,dp)#abhi sell nhi kiya aaga jaka sell karenga
            profit+=max(sellkaro,skip)
        
        dp[index][Buy][limit]=profit
        return dp[index][Buy][limit]

    def maxProfit(self, k, prices): 
        n=len(prices)
        if not prices:
            return 0

        dp=[[[-1 for _ in range(k+1)]for _ in range(2)]for _ in range(n+1)]
        
        return self.Solve(prices,0,1,k,dp)

## Time Complexity - O(2^n)
## Space Complexity - O(n)
        