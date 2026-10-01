class Solution(object):
    def Solve(self,nums,index,capacity,dp):
        #Base Case
        if capacity==0:
            return True
        if index == 0:
            return nums[0]==capacity
        
        if index<0 or capacity<0:
            return False
        #IF value already calculated return 
        if dp[index][capacity] != -1:
            return dp[index][capacity]

        
        #Recursive Case
        include=False
        if nums[index]<=capacity:
            include=self.Solve(nums,index-1,capacity-nums[index],dp)

        exclude=self.Solve(nums,index-1,capacity,dp)

        dp[index][capacity]=include or exclude
        return dp[index][capacity]

    def canPartition(self, nums):
        n=len(nums)
        total=sum(nums)
        if total%2 != 0:
            return False
        capacity=total/2
        #creation of Dp array
        dp=[[-1 for _ in range(capacity + 1)]for _ in range(n)]

        return self.Solve(nums,n-1,capacity,dp)


## By Simple Checking even or Odd:
    #def calPartition(self,nums):
        # n=len(nums)
        # total=0
        # for i in range(n):
        #     total+=nums[i]
        # if total%2==0:
        #     return True
        # else:
        #     return False
    



        