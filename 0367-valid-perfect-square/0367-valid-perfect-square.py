class Solution(object):
    def isPerfectSquare(self, num):
        low=0
        high=num
        answar=0
        while low <= high:
            mid=low+(high-low)//2
            if mid**2==num:
                answar=mid
                return True
            elif mid**2 < num:
                answar=mid
                low=mid+1
            else:
                high=mid-1
        return False


        