class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        #Greedy approach(if prev day price is less then current price then ad the current profit to last profit)
        n=len(prices)
        profit=0

        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit





        