class Solution(object):
    def Solve(self,nums,i,dp):
        if i < 0:
            return 0
        if i == 0:
            return nums[0]
        if dp[i]!=-1:
            return dp[i]
        include=self.Solve(nums,i-2,dp)+nums[i]
        exclude=self.Solve(nums,i-1,dp)+0
        dp[i]=max(include,exclude)
        return dp[i]

    def rob(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        #exclude last house 
        list1=nums[0:n-1]
        dp=[-1]*len(list1)
        case1=self.Solve(list1,n-2,dp)
        #exclude first house
        list2=nums[1:n]
        dp=[-1]*len(list2)
        case2=self.Solve(list2,n-2,dp)
        return max(case1,case2)

        