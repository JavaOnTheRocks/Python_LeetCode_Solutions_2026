class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        has_swapped=True
        while has_swapped:
            has_swapped=False
            for i in range(n-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    has_swapped=True
        return nums
#Bubble Sort - Time Complexity - O(n^2) best case- O(N)
#Space Complexity - O(1)
        # n=len(nums)
        # for i in range(0,n):
        #     min_index=i
        #     for j in range(i+1,n):
        #         if nums[j]<nums[min_index]:
        #             min_index=j
        #     #swapping
        #     nums[i],nums[min_index]=nums[min_index],nums[i]
        # return nums
#Time complexity - O(n^2)  Required optimization
#Space complexity- o(1) inplace modification
