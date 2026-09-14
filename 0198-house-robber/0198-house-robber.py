class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n == 0:#index out of bound 
            return 0
        if n == 1:
            return nums[0]
        dp=[0]*(n)
        dp[0]=nums[0]#from base case
        for i in range(1,n):
            include=dp[i-2]+nums[i]
            exclude=dp[i-1]+0
            dp[i]=max(include,exclude)
        return dp[i]
        
        