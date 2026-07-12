# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    #helper funtion for both ascending or descending order binary search

    def findInMountainArray(self, target, mountainArr):
        n=mountainArr.length()
        low=0
        high=n-1
        while low < high:
            mid = low + (high-low)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                low=mid+1
            else:
                high=mid
        peak=low

        #search in left side arr
        low=0
        high=peak
        while low <= high:
            mid = low + (high-low)//2
            value=mountainArr.get(mid)
            if value==target:
                return mid
            elif value>target:
                high=mid-1
            else:
                low=mid + 1
        
        #Search in right side arr
        low=peak+1
        high=n-1
        while low <= high:
            mid = low + (high-low)//2
            value=mountainArr.get(mid)
            if value==target:
                return mid
            elif value>target:
                low=mid+1
            else:
                high=mid-1
        return -1  

