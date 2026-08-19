import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        m=len(heights)#number of rows
        n=len(heights[0])#number of columns
        effort=[]
        for i in range(m):
            effort.append([float("inf")]*n)
        effort[0][0]=0
        heap=[] #priority queue
        heapq.heappush(heap,(0,0,0)) #effort #row #col
        while heap:
            curr_effort,row,col=heapq.heappop(heap)
            if row==m-1 and col == n-1:
                return curr_effort
            directions = [
                    (-1, 0),   # up
                    (1, 0),    # down
                    (0, -1),   # left
                    (0, 1)     # right      
                ]
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                #check condition:
                if nr<0 or nc<0 or nr>=m or nc>=n:
                    continue#kuch mut karo continue karo loop ko
                    return curr_effort
                edge_effort = abs(heights[row][col] - heights[nr][nc])
                #effort of path
                new_effort=max(curr_effort,edge_effort)
                #Reaxation condition
                if new_effort < effort[nr][nc]:
                    effort[nr][nc]=new_effort
                    heapq.heappush(heap,(new_effort,nr,nc))
        return -1






        

        