class Solution(object):
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
        prev2=0
        prev1=max(bucket[0],bucket[1]) #

        for i in range(2,max_val+1):
            include=prev2+bucket[i]
            exclude=prev1+0
            curr=max(include,exclude)
            prev2=prev1
            prev1=curr

        return prev1



        
        