import heapq
import math
class Solution(object):
    def __init__(self):
        self.heap=[]
    def distance(self,points):
        self.heap=[]
        for point in points:
            dis=(point[0])**2 + (point[1])**2
            # dis=math.sqrt(dis)
            self.heap.append((dis,point))
        heapq.heapify(self.heap)
        
    def kClosest(self, points, k):
        self.distance(points)
        ans=[]
        for i in range(k):
            dis,point=heapq.heappop(self.heap)
            ans.append(point)
        return ans


       

        
        