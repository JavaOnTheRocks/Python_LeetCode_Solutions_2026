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

    def tabulization(self,nums):
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp=[0]*n
        #base case to bottoum 
        prev1=nums[0]
        prev2=0
        for i in range(1,n):
            include=prev2+nums[i]
            exclude=prev1+0
            curr=max(include,exclude)
            prev2=prev1
            prev1=curr
        return prev1     

    def rob(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        #case 1 : exclude last house 
        list1=nums[:n-1]
        case1=self.tabulization(list1)
        #case 2 : exclude first house
        list2=nums[1:]
        case2=self.tabulization(list2)
        return max(case1,case2)
        