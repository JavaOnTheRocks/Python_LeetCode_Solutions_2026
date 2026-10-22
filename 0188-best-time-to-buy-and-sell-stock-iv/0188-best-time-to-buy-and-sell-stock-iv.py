class Solution(object):
    def SolveTab(self,prices,index,Buy,k):
        n=len(prices)

        dp=[[[0 for _ in range(k+1)]for _ in range(2)]for _ in range(n+1)]

        for index in range(n-1,-1,-1):
            for Buy in range(2):
                for limit in range(1,k+1):
                    profit=0
                    #Recursive Approach:(include or Exclude)
                    n=len(prices)
                    if Buy==1:
                        ## Buy
                        buykaro=-prices[index]+dp[index+1][0][limit]
                        ## Skip
                        skip=0+dp[index+1][1][limit]#abhi buy nhi kiya aaga jaka buy kareanga
                        profit+=max(buykaro,skip)

                    else:
                        ## Sell
                        sellkaro=prices[index]+ dp[index+1][1][limit-1]
                        ## Skip
                        skip=0+ dp[index+1][0][limit]#abhi sell nhi kiya aaga jaka sell karenga
                        profit+=max(sellkaro,skip)
                    
                    dp[index][Buy][limit]=profit
        
        return dp[0][1][k]



    def maxProfit(self, k, prices): 
        if not prices:
            return 0
        
        return self.SolveTab(prices,0,1,k)

## Time Complexity - O(n*k)
## Space Complexity - O(n*K)
        