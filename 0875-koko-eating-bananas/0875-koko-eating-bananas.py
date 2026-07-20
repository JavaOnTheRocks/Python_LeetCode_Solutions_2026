from math import ceil
class Solution(object):
    def minEatingSpeed(self, piles, h):
        n=len(piles)
        low=1
        high=max(piles)
        while low<high:
                mid = low + (high-low)//2

                total_hour=0
                for pile in piles:  
                    # hour=ceil(float(pile)/mid) this will perfom float devision and import required 
                    hour=(pile+mid-1)//mid
                    total_hour+=hour

                if total_hour<=h:
                    high=mid
                else:
                    low=mid+1
        return low

       
        