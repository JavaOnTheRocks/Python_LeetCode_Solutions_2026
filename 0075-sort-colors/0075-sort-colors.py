class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(0,n):
            min_index=i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            #swapping
            nums[i],nums[min_index]=nums[min_index],nums[i]
        return nums
 
        