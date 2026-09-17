class Solution(object):
    def Solve(self,nums,i,dp):
        if i<0:
            return 0
        if i==0:
            return 0
        if dp[i]!=-1:
            return dp[i]
        include=self.Solve(nums,i-2,dp)+nums[i]
        exclude=self.Solve(nums,i-1,dp)+0
        dp[i]=max(include,exclude)
        return dp[i]

    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        
        #transform into house robber array 
        max_val=max(nums)
        bucket=[0]*(max_val+1)
        for num in nums:
            bucket[num]+=num
        dp=[-1]*len(bucket)
        return self.Solve(bucket,max_val,dp)



        
        