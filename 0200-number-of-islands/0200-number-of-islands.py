class Solution(object):
    def dfs(self,row,col,grid,m,n,visited):
        #base returning condition
        if row<0 or row>=m or col<0 or col>=n:
            return
        if grid[row][col]=="0":
            return
        if visited[row][col]:#if already visited return
            return
        #visited 
        visited[row][col]=True
        #recursive neighbour exploring condition
        self.dfs(row-1,col,grid,m,n,visited)
        self.dfs(row,col+1,grid,m,n,visited)
        self.dfs(row+1,col,grid,m,n,visited)
        self.dfs(row,col-1,grid,m,n,visited)
        
    def numIslands(self, grid):
        island=0
        m=len(grid)
        n=len(grid[0])
        visited=[]
        for i in range(m):
            visited.append([False]*n)
        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1" and not visited[row][col]:#find unvisted land and calulate the all islands
                    self.dfs(row,col,grid,m,n,visited)
                    island+=1
        return island
             
        


    