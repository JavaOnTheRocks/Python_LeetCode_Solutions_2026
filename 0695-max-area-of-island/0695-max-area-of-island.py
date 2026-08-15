class Solution(object):
    def dfs(self,row,col,grid,visited,m,n):
        #base case:
        if row<0 or col<0 or row>=m or col>=n:
            return 0
        if grid[row][col]==0:
            return 0

        if visited[row][col]:
            return 0
        visited[row][col]=True

        area=1 #current land cell contribute 1 area
        #explore all neighbour recursilivy
        area+=self.dfs(row-1,col,grid,visited,m,n)#up
        area+=self.dfs(row+1,col,grid,visited,m,n)#down
        area+=self.dfs(row,col-1,grid,visited,m,n)#left
        area+=self.dfs(row,col+1,grid,visited,m,n)#right
        return area

    def maxAreaOfIsland(self, grid):
        max_area=0
        m=len(grid)#number of rows
        n=len(grid[0])#number of column
        visited=[]
        for i in range(m):
            visited.append([False]*n)
        for row in range(m):
            for col in range(n):
                area=self.dfs(row,col,grid,visited,m,n)
                max_area=max(max_area,area)
        return max_area
                





        
        