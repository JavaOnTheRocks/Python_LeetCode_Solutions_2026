class Solution(object):
    #Fee constent and vary nhi ker raha
    def SolveTab(self,prices,index,Buy,fee):
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
                    sellkaro=prices[index]-fee+next[1]
                    ## Skip
                    skip=0+next[0]#abhi sell nhi kiya aaga jaka sell karenga
                    profit+=max(sellkaro,skip)  
                curr[Buy]=profit
            next=curr

        return next[1]

    def maxProfit(self, prices, fee):
        if not prices:
            return 0

        return self.SolveTab(prices,0,1,fee)

## Time Complexity : O(n)
## Space Complexity : O(1)