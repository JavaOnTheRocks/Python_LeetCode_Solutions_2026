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
        if len(nums)==1:
            return nums[0]
        #transform into house robber array 

        max_val=max(nums)
        bucket=[0]*(max_val+1)
        for num in nums:
            bucket[num]+=num
            
        dp=[0]*len(bucket)
        #Base case
        dp[0]=0
        dp[1]=max(bucket[0],bucket[1]) #

        for i in range(2,max_val+1):
            include=dp[i-2]+bucket[i]
            exclude=dp[i-1]+0
            dp[i]=max(include,exclude)

        return dp[max_val]



        
        