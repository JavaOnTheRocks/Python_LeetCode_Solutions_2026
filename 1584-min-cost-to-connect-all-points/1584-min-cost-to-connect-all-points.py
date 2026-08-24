import heapq
class Solution(object):#we will solve without building the graph
    def minCostConnectPoints(self, points):
        n=len(points)
        min_cost=0
        inMST=set()
        #inMST=[False]*n # for this we also have to caeck how much we have visted till now in MST
        heap=[]
        heapq.heappush(heap,(0,0))

        while len(heap)>0:
            wt,u=heapq.heappop(heap)

            if u in inMST:
                continue

            inMST.add(u)
            min_cost+=wt
            #dynamically check for the neighbour 
            for v in range(n):
                if v not in inMST:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap,(dist,v))       
        return min_cost
        