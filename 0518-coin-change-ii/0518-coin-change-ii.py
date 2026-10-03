class Solution(object):
    def helper(self,nums,index,target,dp):
        n=len(nums)
        #Base Case
        if target == 0:
            return 1
        if target < 0:
            return 0
        if index == n:
            return 0
        if dp[index][target] != -1:
            return dp[index][target]
        #recursive Case to fins all possible combination:
        #include
        include=self.helper(nums,index,target-nums[index],dp)
        #Exclude
        exclude=self.helper(nums,index+1,target,dp)
        dp[index][target]=include + exclude
        return dp[index][target]

    def change(self, amount, coins):
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n+1)]
        return self.helper(coins,0,amount,dp)        