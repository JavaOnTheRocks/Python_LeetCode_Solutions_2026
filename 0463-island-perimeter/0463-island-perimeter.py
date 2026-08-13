class Solution(object):
    def dfs(self,row,col,grid,m,n,visited):
        #base case
        if row<0 or row >= m or col<0 or col >= n:#boundry will contribute in parameter
            return 1
        if grid[row][col]==0:
            return 1
        #already visite land
        if visited[row][col]:
            return 0
        #track visited
        visited[row][col]=True


        #Neighbour visiting tecursive case
        parimeter=(self.dfs(row-1,col,grid,m,n,visited)+
        self.dfs(row+1,col,grid,m,n,visited)+
        self.dfs(row,col-1,grid,m,n,visited)+
        self.dfs(row,col+1,grid,m,n,visited))
        return parimeter
        
    def islandPerimeter(self, grid):
        m=len(grid)
        n=len(grid[0])
        visited=[]        
        for i in range(m):
            visited.append([False]*n)
        #find land cell and start bfs
        for row in range(m):
            for col in range(n):
                if grid[row][col]==1:
                    return self.dfs(row,col,grid,m,n,visited)



        