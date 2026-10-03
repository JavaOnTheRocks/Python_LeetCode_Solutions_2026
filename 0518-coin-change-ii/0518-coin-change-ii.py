class Solution(object):
    def change(self, amount, coins):
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n+1)]
        #Base Case:
        for index in range(n+1):
            dp[index][0]=1
        #Itratively sub cell ko bhrenga:
        for index in range(n-1,-1,-1):
            for amount in range(1,amount+1):
                include=0
                if amount-coins[index] >= 0:
                    include=dp[index][amount-coins[index]]#its depend on the past amount

                exclude=dp[index+1][amount]#it is based on future so we have to run the Loop Backword

                dp[index][amount]=include+exclude

        return dp[0][amount]  