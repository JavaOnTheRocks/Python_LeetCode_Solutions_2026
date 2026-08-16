from collections import deque
class Solution(object):
    def bfs(self,q,grid,m,n,frash):
        time=0 #sara exisiting rotten orenges append ho jaynga
        while q:
            row,col,curr_time=q.popleft()
            time=max(time,curr_time)

            #check UP
            if row-1 >= 0 and grid[row-1][col]==1:
                grid[row-1][col]=2
                frash-=1
                q.append((row-1,col,curr_time+1)) #append only takes one object
            #check RIGHT
            if col+1 < n and grid[row][col+1]==1:
                grid[row][col+1]=2
                frash-=1
                q.append((row,col+1,curr_time+1))
            #check LEFT
            if col-1>=0 and grid[row][col-1]==1:
                grid[row][col-1]=2
                frash-=1
                q.append((row,col-1,curr_time+1))
            #check DOWN
            if row+1<m and grid[row+1][col]==1:
                grid[row+1][col]=2
                frash-=1
                q.append((row+1,col,curr_time+1))
        return time,frash

        
    def orangesRotting(self, grid):
        m=len(grid)#number of rows
        n=len(grid[0])#number of column
        q=deque()
        frash=0
        for row in range(m):#Multisource BFS
            for col in range(n):
                if grid[row][col]==2:
                    q.append((row,col,0))  #already rotten hato time 0 sec
                if grid[row][col]==1:
                    frash+=1       
        #call BFS
        time,frash=self.bfs(q,grid,m,n,frash)
        if frash>0:
            return -1
        return time
        


        

        
        