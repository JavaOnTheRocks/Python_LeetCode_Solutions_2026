class Solution(object):
    def shipWithinDays(self, weights, days):
        n=len(weights)
        low=max(weights)
        high=sum(weights)
        while low < high:
            mid=low+(high-low)//2
            day=1
            currload=0
            for pakage in weights:
                if currload + pakage <= mid:
                    currload+=pakage
                else:
                    day+=1
                    currload=pakage
            if day <= days:
                high=mid
            else:
                low=mid+1
        return low

        