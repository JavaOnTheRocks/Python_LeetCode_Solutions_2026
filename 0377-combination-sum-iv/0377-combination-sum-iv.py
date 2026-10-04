class Solution(object):
    def Solve(self,nums,target,dp):
        n=len(nums)
        ## Base Case:
        if target==0:
            return 1
        if target < 0:
            return 0 
        if dp[target] != None:
            return dp[target]
        count=0
        #Recursive Case(we have to get all possible caombination included duplicates)
        for num in nums:
            count+=self.Solve(nums,target-num,dp)
        dp[target]=count
        return dp[target]

    def combinationSum4(self, nums, target):
        n=len(nums)
        dp=[None]*(target+1)
        return self.Solve(nums,target,dp)



        