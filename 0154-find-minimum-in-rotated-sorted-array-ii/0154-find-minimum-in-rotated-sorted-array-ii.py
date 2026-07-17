class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1

        while low<high:
            mid=low + (high-low)//2
            if nums[low]<nums[high]:
                return nums[low]
            else:
                if nums[mid]==nums[high]:
                    high-=1
                elif nums[mid] > nums[high]:
                    low=mid+1
                else:
                    high=mid
        return nums[low]

            


   
        