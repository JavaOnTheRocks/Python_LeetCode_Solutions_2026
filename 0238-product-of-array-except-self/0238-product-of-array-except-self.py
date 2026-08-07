class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        left=[]
        left_prefix=1
        for i in range(n):
            left.append(left_prefix)
            left_prefix*=nums[i]

        right=[]
        right_prefix=1
        for i in range(n-1,-1,-1):
            right.append(right_prefix)
            right_prefix*=nums[i]

        right.reverse()
        answer=[]
        for i in range(n):
            answer.append(left[i]*right[i])
        return answer

           
        