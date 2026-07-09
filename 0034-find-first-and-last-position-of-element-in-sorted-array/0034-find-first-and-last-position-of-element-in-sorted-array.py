class Solution(object):
    def FirstOccurance(self,nums,target):
        start=0
        end=len(nums)-1
        firstOccurance=-1
        while start <= end:
            mid= end + (start-end)//2
            if nums[mid]==target:
                firstOccurance=mid
                end=mid-1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return firstOccurance

    def LastOccurance(self,nums,target):
        start=0
        end=len(nums)-1
        lastOccurance=-1
        while start <= end:
            mid = end + (start-end)//2
            if nums[mid]==target:
                lastOccurance=mid
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return lastOccurance
        

    def searchRange(self, nums, target):
        return [self.FirstOccurance(nums,target),self.LastOccurance(nums,target)]

               
        