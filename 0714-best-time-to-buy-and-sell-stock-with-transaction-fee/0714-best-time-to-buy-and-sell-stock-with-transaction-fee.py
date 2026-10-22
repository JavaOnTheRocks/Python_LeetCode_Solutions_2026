class Solution(object):
    #Fee constent and vary nhi ker raha
    def Solve(self,prices,index,Buy,fee,dp):
        if index == len(prices):
            return 0

        if dp[index][Buy] != -1:
            return dp[index][Buy]

        profit=0
        #Recursive Approach:(include or Exclude)
        n=len(prices)
        if Buy==1:
            ## Buy
            buykaro=-prices[index]+self.Solve(prices,index+1,0,fee,dp)
            ## Skip
            skip=0+self.Solve(prices,index+1,1,fee,dp)#abhi buy nhi kiya aaga jaka buy kareanga
            profit+=max(buykaro,skip)

        else:
            ## Sell
            sellkaro=prices[index]-fee+self.Solve(prices,index+1,1,fee,dp)
            ## Skip
            skip=0+self.Solve(prices,index+1,0,fee,dp)#abhi sell nhi kiya aaga jaka sell karenga
            profit+=max(sellkaro,skip)
        
        dp[index][Buy]=profit
        return dp[index][Buy]

    def maxProfit(self, prices, fee):
        n=len(prices)
        if not prices:
            return 0
        dp=[[-1 for _ in range(2)]for _ in range(n+1)]

        return self.Solve(prices,0,1,fee,dp)

## Time Complexity : O(n)
## Space Complexity : O(n)+O(n) Recursive Stack