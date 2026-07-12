class Solution(object):
    def peakIndexInMountainArray(self, arr):
        #Binary search appraoch
        low=0
        high=len(arr)-1
        while low < high:#jub bhi braber or baad ho gya low then loop end 
            mid = low + (high-low)//2
            if arr[mid] < arr[mid+1]:
                low=mid+1
            else:
                high=mid
        return low
            
