class Solution(object):
    def SolveTabSO(self,prices,index,Buy):
        n=len(prices)
        curr=[0,0]
        next=[0,0]
        
        #Itrative appraoch:
        for index in range(n-1,-1,-1):
            for Buy in range(2):
                profit=0
                #Recursive Approach:(include or Exclude)
                if Buy==1:
                    ## Buy
                    buykaro=-prices[index]+next[0]
                    ## Skip
                    skip=0+next[1]#abhi buy nhi kiya aaga jaka buy kareanga
                    profit+=max(buykaro,skip)

                else:
                    ## Sell
                    sellkaro=prices[index]+next[1]
                    ## Skip
                    skip=0+next[0]#abhi sell nhi kiya aaga jaka sell karenga
                    profit+=max(sellkaro,skip)  
                curr[Buy]=profit
            next=curr
        return next[1]

    def maxProfit(self, prices):
        n=len(prices)
        if not prices:
            return 0 

        return self.SolveTabSO(prices,n-1,1)#pahala Buy karna tabhi to baad ma sell ker paunga

## Time Complexity - O(N)
## Space Complexity - O(1)