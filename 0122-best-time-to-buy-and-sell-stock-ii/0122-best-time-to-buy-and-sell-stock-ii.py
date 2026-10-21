class Solution(object):
    def SolveTab(self,prices,index,Buy):
        n=len(prices)
        dp=[[0 for _ in range(n+1)]for _ in range(2)] # initallized wiht 0 ont havet o handle Base Case
        

        #Itrative appraoch:
        for index in range(n-1,-1,-1):
            for Buy in range(2):
                profit=0
                #Recursive Approach:(include or Exclude)
                if Buy==1:
                    ## Buy
                    buykaro=-prices[index]+dp[0][index+1]
                    ## Skip
                    skip=0+dp[1][index+1]#abhi buy nhi kiya aaga jaka buy kareanga
                    profit+=max(buykaro,skip)

                else:
                    ## Sell
                    sellkaro=prices[index]+dp[1][index+1]
                    ## Skip
                    skip=0+dp[0][index+1]#abhi sell nhi kiya aaga jaka sell karenga
                    profit+=max(sellkaro,skip)  
                dp[Buy][index]=profit

        return dp[1][0]

    def maxProfit(self, prices):
        n=len(prices)
        if not prices:
            return 0 

        return self.SolveTab(prices,n-1,1)#pahala Buy karna tabhi to baad ma sell ker paunga

## Time Complexity - O(N) Exponential  TLE
## Space Complexity - O(N) dp Space 