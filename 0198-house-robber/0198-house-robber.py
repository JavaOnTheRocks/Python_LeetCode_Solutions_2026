class Solution(object):
    def solve(self,nums,i,dp):
        #base case
        if i < 0:#index out of bound 
            return 0
        if i == 0:
            return nums[0]
        if dp[i] != -1:
            return dp[i]
        #recursive case
        include=self.solve(nums,i-2,dp)+nums[i]
        exclude=self.solve(nums,i-1,dp)+0
        dp[i]=max(include,exclude)
        return dp[i]

    def rob(self, nums):
        n=len(nums)
        dp=[-1]*(n+1)
        return self.solve(nums,n-1,dp)#last index pa khada ha initally
        
        