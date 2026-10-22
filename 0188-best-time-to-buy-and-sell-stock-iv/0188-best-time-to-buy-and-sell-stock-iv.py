class Solution(object):
    def SolveSpace(self,prices,index,Buy,k):
        n=len(prices)

        curr=[[0 for _ in range(k+1)]for _ in range(2)]
        next=[[0 for _ in range(k+1)]for _ in range(2)]

        for index in range(n-1,-1,-1):
            for Buy in range(2):
                for limit in range(1,k+1):
                    profit=0
                    #Recursive Approach:(include or Exclude)
                    n=len(prices)
                    if Buy==1:
                        ## Buy
                        buykaro=-prices[index]+next[0][limit]
                        ## Skip
                        skip=0+next[1][limit]#abhi buy nhi kiya aaga jaka buy kareanga
                        profit+=max(buykaro,skip)

                    else:
                        ## Sell
                        sellkaro=prices[index]+ next[1][limit-1]
                        ## Skip
                        skip=0+ next[0][limit]#abhi sell nhi kiya aaga jaka sell karenga
                        profit+=max(sellkaro,skip)
                    
                    curr[Buy][limit]=profit
            next=curr
        
        return next[1][k]



    def maxProfit(self, k, prices): 
        if not prices:
            return 0
        
        return self.SolveSpace(prices,0,1,k)

## Time Complexity - O(n*k)
## Space Complexity - O(K)
        