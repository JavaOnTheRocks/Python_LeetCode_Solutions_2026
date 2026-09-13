class Solution(object):
    def solveRec(self,coins,amount,memo):
        #base case
        if amount==0:
            return 0

        if amount < 0:
            return float("inf")

        if amount in memo:#if amount already exist in memo
            return memo[amount]

        minCount=float("inf")
        for coin in coins:
            res=self.solveRec(coins,amount-coin,memo)

            if res != float("inf"):   #we are just saving from chaking becouse min hi min rah jayega is case ma
                minCount=min(minCount,res+1) 
        memo[amount]=minCount
        return minCount
    def coinChange(self, coins, amount):
        memo={}
        ans=self.solveRec(coins,amount,memo)
        if ans == float("inf"):
            return -1
        return ans


        