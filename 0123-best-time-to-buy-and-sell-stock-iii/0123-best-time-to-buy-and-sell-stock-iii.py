class Solution(object):
    def SolveTab(self,prices):
        n=len(prices)
        dp=[[[0 for _ in range(3)]for _ in range(2)]for _ in range(n+1)]
        #Handle Base Case
        #Iteraticve approach
        for index in range(n-1,-1,-1):
            for Buy in range(2):
                # Start from 1 because limit = 0 means 0 profit remaining anyway
                for limit in range(1,3):
                    profit=0
                    #Recursive Approach:(include or Exclude)
                    if Buy==1:
                        ## Buy
                        buykaro=-prices[index]+dp[index+1][0][limit]
                        ## Skip
                        skip=0+dp[index+1][1][limit]#abhi buy nhi kiya aaga jaka buy kareanga
                        profit+=max(buykaro,skip)

                    else:
                        ## Sell
                        sellkaro=prices[index]+dp[index+1][1][limit-1]
                        ## Skip
                        skip=0+dp[index+1][0][limit]#abhi sell nhi kiya aaga jaka sell karenga
                        profit+=max(sellkaro,skip)
                    
                    dp[index][Buy][limit]=profit

        return dp[0][1][2]


    def maxProfit(self, prices):
        if not prices:
            return 0
        
        return self.SolveTab(prices)

## Time Complexity - O(n)
## Sapce Complexity - O(n)

    