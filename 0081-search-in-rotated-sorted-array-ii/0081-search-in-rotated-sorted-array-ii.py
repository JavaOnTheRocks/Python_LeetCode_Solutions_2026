class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1

        while low <= high:
            mid = low + (high-low)//2

            if nums[mid]==target:
                return True
                
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue #Becaue still mid to wahi hi rahega na to yahi acontinue raknho new compute mut karo

            #left half is sorted 
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False