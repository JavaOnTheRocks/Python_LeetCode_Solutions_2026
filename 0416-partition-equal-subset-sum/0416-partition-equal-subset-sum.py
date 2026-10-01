class Solution(object):
    def canPartition(self, nums):
        n=len(nums)
        total=sum(nums)
        if total%2 != 0:
            return False
        capacity=total/2
        #creation of 1-D,Dp array
        curr=[False for _ in range(capacity+1)]

        ## Base Case:
        ## the capacity == 0 is always true, so we can initialize the first column of the dp array to True
        curr[0]=True

        #check if the first value os less then or equal to the target capacity-
        if nums[0]<=capacity:
            curr[nums[0]]=True
        
        for index in range(1,n):
            for cap in range(capacity,-1,-1):

                #Recursive Case
                include=False
                if nums[index]<=cap:
                    include=curr[cap-nums[index]]

                exclude=curr[cap]

                curr[cap]=include or exclude
                
        return curr[capacity]


    



        