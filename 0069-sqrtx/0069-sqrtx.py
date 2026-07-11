class Solution(object):
    def mySqrt(self, x):
        low=0
        high=x
        answar=x
        while low <= high:
            mid=low + (high-low)//2
            if mid ** 2==x:
                answar = mid
                return answar #excect value milta hi stop
            elif mid**2<x:
                answar=mid
                low=mid+1
            else:
                high=mid-1
        return answar