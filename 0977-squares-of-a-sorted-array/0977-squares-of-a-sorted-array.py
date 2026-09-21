class Solution(object):
    def makesquare(self,nums):
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]*nums[i]
        return nums
    def sortedSquares(self, nums):
        n=len(nums)
        self.makesquare(nums)
##USING Python in build Sort() - O(NlogN)
        nums.sort()
        return nums

## Using Selection sort:-
        # for i in range(n):
        #     min_index=i
        #     for j in range(i+1,n):
        #         if nums[j]<nums[min_index]:
        #             min_index=j
        #     nums[i],nums[min_index]=nums[min_index],nums[i]
        # return nums


# Time Complexity- O(N^2)+O(n) Becouse of Selection sort Algorithum
## Require Optimization....
# Option 1 :
# use python in Build sort - time complexity will be O(NlogN) Timsort
# Space complexity - O(1)
        
        