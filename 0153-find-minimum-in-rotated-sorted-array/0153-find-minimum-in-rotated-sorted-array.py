class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1

        while low < high:
            mid= low + (high-low)//2

            if nums[low]<=nums[high]:
                return nums[low]

            else:
                #right side ma ho min element 
                if nums[mid]>nums[high]:
                    low=mid+1
                else:#minimum left ma ha ya mid pa ha 
                    high=mid

        return nums[low]




