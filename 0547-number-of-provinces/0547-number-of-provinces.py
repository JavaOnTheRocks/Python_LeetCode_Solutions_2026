class Solution(object):
    def dfs(self,node,adjMatrix,visited):
        visited[node]=True
        for x in range(len(adjMatrix[0])):
            if adjMatrix[node][x]==1 and not visited[x]:#curent node/ khud connected ha to usma ya visited dikha dega
                self.dfs(x,adjMatrix,visited)

        #base case
        # if row<0 or row>=m or col<0 or col>=n:
        #     return
        # if isConnected[row][col]==0:
        #     return 
        # if visited[row][col]:
        #     return
        # visited[row][col]=True
        # # Explore all the neighbour using Recursion
        # self.dfs(row-1,col,m,n,isConnected,visited)#up
        # self.dfs(row+1,col,m,n,isConnected,visited)#down
        # self.dfs(row,col+1,m,n,isConnected,visited)#right
        # self.dfs(row,col-1,m,n,isConnected,visited)#left

    def findCircleNum(self, isConnected):
        n=len(isConnected)
        visited=[False]*n
        ans=0
        for i in range(n):
            if not visited[i]:
                self.dfs(i,isConnected,visited)
                ans+=1
        return ans
        # count=0
        # m=len(isConnected)#number of rows
        # n=len(isConnected[0])#number of columns
        # visited=[]
        # for i in range(m):
        #     visited.append([False]*n)
        # for row in range(m):
        #     for col in range(n):
        #         if isConnected[row][col]==1 and not visited[row][col]:
        #             self.dfs(row,col,m,n,isConnected,visited)
        #             count+=1
        # return count

        
        