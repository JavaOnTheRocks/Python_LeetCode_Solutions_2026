class Solution(object):
    # def helper(self,nums,index,target):
    #     n=len(nums)
    #     #Base Case
    #     if target == 0:
    #         return 0
    #     if target < 0:
    #         return float("inf")
    #     if index == n:
    #         return float("inf")
        
    #     minCount=float("inf")
    #     #recursive Case to find all possible combination:
    #     #include
    #     include=self.helper(nums,index,target-nums[index])
    #     minCount=min(minCount,include+1)
    #     #Exclude
    #     exclude=self.helper(nums,index+1,target)
    #     minCount=min(minCount,exclude) #if we are excludeng an coin thaen why we count taht coin
    #     return minCount

    def helper(self,nums,target,dp):
        n=len(nums)
        #Base Case
        if target == 0:
            return 0 #0 ko banan ma 0 coins ki requirement ha
        if target < 0:
            return float("inf")

        minCount=float("inf")
        if dp[target] != -1:
            return dp[target]

        ## in This Appraoch i am trying each and Every Possible Combination
        for num in nums:
            result=self.helper(nums,target-num,dp)
            if result != float("inf"):
                minCount=min(minCount,result+1,dp)#khud us pahel oin ko bhi to jodna padega

        dp[target]=minCount
        return dp[target]

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



    #def coinChange(self, coins, amount):
        # dp=[float("inf")]*(amount+1)
        # dp[0]=0
        # for i in range(1,amount+1):
        #     for coin in coins:
        #         if i - coin >= 0:
        #             res=dp[i-coin]
        #             if res != float("inf"):
        #                 dp[i]=min(res+1,dp[i])
        # if dp[amount]==float("inf"):
        #     return -1
        # return dp[amount]

        