class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        min_buy=prices[0]
        profit=0

        for i in range(1,n):
            diff=prices[i]-min_buy
            profit=max(profit,diff)
            min_buy=min(min_buy,prices[i])
        
        return profit

## Time Complexity - O(N)
## Space Complexity - O(1)

    
        
        