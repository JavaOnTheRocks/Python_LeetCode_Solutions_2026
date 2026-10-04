class Solution(object):
    def combinationSum4(self, nums, target):
        n=len(nums)
        dp=[0]*(target+1)
        dp[0]=1
        for t in range(1,target+1):
            for num in nums:
                if t-num>=0:
                    dp[t]+=dp[t-num]
        return dp[target]
        