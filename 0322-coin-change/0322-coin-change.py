class Solution(object):
    def solveRec(self,coins,amount,dp):
        #base case
        if amount==0:
            return 0

        if amount < 0:
            return float("inf")

        if dp[amount] != -1:#if amount already exist in memo
            return dp[amount]

        minCount=float("inf")
        for coin in coins:
            res=self.solveRec(coins,amount-coin,dp)

            if res != float("inf"):   #we are just saving from chaking becouse min hi min rah jayega is case ma
                minCount=min(minCount,res+1) 
        dp[amount]=minCount
        return minCount
    def coinChange(self, coins, amount):
        dp=[-1]*(amount+1)
        ans=self.solveRec(coins,amount,dp)
        if ans == float("inf"):
            return -1
        return ans

        