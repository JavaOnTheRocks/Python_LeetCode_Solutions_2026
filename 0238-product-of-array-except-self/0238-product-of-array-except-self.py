class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        answer=[1]*n
        left_prefix=1
        for i in range(n):
            answer[i]*=left_prefix
            left_prefix*=nums[i]

        right_prefix=1
        for i in range(n-1,-1,-1):
            answer[i]*=right_prefix
            right_prefix*=nums[i]

        return answer

           
        