class Solution(object):
    def SolveTab(self,prices):
        n=len(prices)
        #coll nder and row baher define karo:
        curr=[[0 for _ in range(3)]for _ in range(2)]
        next=[[0 for _ in range(3)]for _ in range(2)]
        #Iteraticve approach
        for index in range(n-1,-1,-1):
            for Buy in range(2):
                # Start from 1 because limit = 0 means 0 profit remaining anyway
                for limit in range(1,3):
                    profit=0
                    #Recursive Approach:(include or Exclude)
                    if Buy==1:
                        ## Buy
                        buykaro=-prices[index]+next[0][limit]
                        ## Skip
                        skip=0+next[1][limit]#abhi buy nhi kiya aaga jaka buy kareanga
                        profit+=max(buykaro,skip)

                    else:
                        ## Sell
                        sellkaro=prices[index]+next[1][limit-1]
                        ## Skip
                        skip=0+next[0][limit]#abhi sell nhi kiya aaga jaka sell karenga
                        profit+=max(sellkaro,skip)
                    
                    curr[Buy][limit]=profit
            next=curr

        return next[1][2]


    def maxProfit(self, prices):
        if not prices:
            return 0
        
        return self.SolveTab(prices)

## Time Complexity - O(n)
## Sapce Complexity - O(1)

    