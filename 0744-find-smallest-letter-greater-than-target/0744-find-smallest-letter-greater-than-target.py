class Solution(object):
    def UpperBound(self,nums,target):
        low=0
        high=len(nums)-1
        answar=len(nums)
        while low <= high:
            mid=low + (high-low)//2
            if nums[mid] > target:
                answar=mid
                high=mid-1
            else:
                low=mid+1
        return answar
    def nextGreatestLetter(self, letters, target):
        index = self.UpperBound(letters, target)
        if index == len(letters):#yaha choti values ko bhi 
            return letters[0]
        return letters[index]
        
        