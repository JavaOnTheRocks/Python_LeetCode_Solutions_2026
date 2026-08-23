from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adjList=[]
        for i in range(n):
            adjList.append([])
        for edge in flights:
            u=edge[0]
            v=edge[1]
            wt=edge[2]
            adjList[u].append((v,wt))#giretion edges
        
        q = deque()
        distance=[float("inf")]*n
        distance[src]=0
        q.append((src,0,0))

        while len(q)>0:
            u,cost,currstop=q.popleft()
            if currstop > k:
                continue#agga k kuch bhi run mut karo
            for neighbour in adjList[u]:
                v,wt=neighbour
                if distance[v]>cost+wt:
                    distance[v]=cost+wt
                    q.append((v,distance[v],currstop+1))

        if distance[dst] != float("inf"):       
            return distance[dst]
        else:
            return -1


        
        #we will use bellamnsan use direct edges
        # distance=[float("inf")]*n
        # distance[src]=0
        # #edge relaxation n-1 times 
        # for i in range(K+1):
        #     for u,v,weight in flights:
        #         if distance[u] != float("inf"):
        #             new_distance=distance[u]+weight
        #             if new_distance < distance[v]:
        #                 distance[v]=new_distance
        # for u,v,wt in flights:
        #     if distance[u] != float("inf"):
        #         if distance[u]+wt < distance[v]:
        #             return -1
        # return distance[dst]
        
        