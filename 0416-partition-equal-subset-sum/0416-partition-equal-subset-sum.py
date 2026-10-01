class Solution(object):
    def canPartition(self, nums):
        n=len(nums)
        total=sum(nums)
        if total%2 != 0:
            return False
        capacity=total/2
        #creation of Dp array
        dp=[[False for _ in range(capacity + 1)]for _ in range(n)]

        ## Base Case:
        ## the capacity == 0 is always true, so we can initialize the first column of the dp array to True
        for i in range(n):
            dp[i][0]=True
        #check if the first value os less then or equal to the target capacity-
        if nums[0]<=capacity:
            dp[0][nums[0]]=True
        
        for index in range(1,n):
            for cap in range(1,capacity + 1):

                #Recursive Case
                include=False
                if nums[index]<=cap:
                    include=dp[index-1][cap-nums[index]]

                exclude=dp[index-1][cap]

                dp[index][cap]=include or exclude

        return dp[n-1][capacity]


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
    



        