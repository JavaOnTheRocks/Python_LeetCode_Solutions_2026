import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        h=[]
        for x in stones:
            heapq.heappush(h,-x)

        while len(h)>1:
            x= -heapq.heappop(h) # oargetst stone fro max heap 
            y= -heapq.heappop(h) # 2nd largetst stone from max heap

            difference=x-y

            if difference > 0:
                heapq.heappush(h,-difference)
        if len(h)==0:
            return 0
        else:
            return -h[0]