class Solution(object):
        
    def DFS(self,i,destination,adjList,visited):
        if i==destination: #ager destintion tuk pahunch gya mutlab path exist karta ha
            return True
        visited[i]=True
        for neighbor in adjList[i]:
            if not visited[neighbor]:
                if self.DFS(neighbor,destination,adjList,visited): #this will leads us to explore all neighbor 
                    return True
        return False#pura for loop hon ka baad bhi nhi mila then retun False
    def validPath(self, n, edges, source, destination):
        #Edge case same hi jagha pe ho to
        if source == destination:
            return True
        adjList=[]
        for i in range(n):
            adjList.append([])
        for edge in edges:
            x=edge[0]
            y=edge[1]
            adjList[x].append(y)
            adjList[y].append(x)

        visited=[False]*n #isko seen set sa bhi ker sakta ha seen=set() seen.add(source)

        return self.DFS(source,destination,adjList,visited)
                    
        # We can also solve this with BFS appraoch

        # adjMatrix=[]
        # for i in range(n):
        #     adjMatrix.append([0]*n)

        # for edge in edges:
        #     x=edge[0]
        #     y=edge[1]   

        #     adjMatrix[x][y]=1
        #     adjMatrix[y][x]=1

        # if adjMatrix[source][destination]==1:
        #     return True
        # else:
        #     return False
