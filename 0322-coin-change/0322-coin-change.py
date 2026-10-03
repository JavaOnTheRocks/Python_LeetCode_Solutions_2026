class Solution(object):
    def coinChange(self, coins, amount):
        n=len(coins)
        #dp is crated th min count for each amount 
        dp=[float("inf")]*(amount+1)
        #Base Case-
        dp[0]=0

        #Now solve iteratively - 
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >= 0:
                    result=dp[i-coin]
                    if result != float("inf"):
                        dp[i]=min(dp[i],result+1)
                    
        #ans = self.helper(coins,0,amount)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
