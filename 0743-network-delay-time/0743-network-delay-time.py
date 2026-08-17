import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        adjList=[]
        for i in range(n+1): #index 0 is simply unused
            adjList.append([])
        for edge in times:
            x=edge[0]
            y=edge[1]
            w=edge[2]
            adjList[x].append((y,w))#directed graph

        distance=[float("inf")]*(n+1)

        #find the soerted disace of all the nodes from source node
        distance[k]=0
        heap=[]
        heapq.heappush(heap,(distance[k],k))

        while len(heap)>0:
            curr_dis,u=heapq.heappop(heap)
            #Is node ka liya adjcesnt/neighbour node konsi ha
            for v,w in adjList[u]:
            #edge Relaxation(helps to store the sorted path between source and destination)
                new_dis=curr_dis + w
                if new_dis < distance[v]:
                    distance[v]=new_dis
                    heapq.heappush(heap,(distance[v],v))
        if float("inf") in distance[1:]:
            return -1 
        return max(distance[1:])#becouse index 0 is simply unused