class Solution(object):
    def validPath(self, n, edges, source, destination):
        adjList=[]
        for i in range(n):
            adjList.append([])
        for edge in edges:
            x=edge[0]
            y=edge[1]
            adjList[x].append(y)
            adjList[y].append(x)

        visited=[False]*n
        def DFS(i,parent,adjList,visited):
            if i==destination:
                return True
            visited[i]=True
            for neighbor in adjList[i]:
                if not visited[neighbor]:
                    if DFS(neighbor,i,adjList,visited):
                        return True
            return False
        return DFS(source,-1,adjList,visited)
                    

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
