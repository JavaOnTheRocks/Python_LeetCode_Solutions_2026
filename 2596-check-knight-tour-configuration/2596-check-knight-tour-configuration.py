class Solution(object):
    def isValid(self,grid,row,col,n,expectedvalue):
        #Base Case
        if row<0 or col<0 or row>=n or col >= n or grid[row][col] != expectedvalue:
            return False

        if expectedvalue == (n)**2-1:
            return True

        #Recurive Case
        #All 8 expected Move:
        ans1=self.isValid(grid,row-2,col+1,n,expectedvalue+1)
        ans2=self.isValid(grid,row-1,col+2,n,expectedvalue+1)
        ans3=self.isValid(grid,row+1,col+2,n,expectedvalue+1)
        ans4=self.isValid(grid,row+2,col+1,n,expectedvalue+1)
        ans5=self.isValid(grid,row+2,col-1,n,expectedvalue+1)
        ans6=self.isValid(grid,row+1,col-2,n,expectedvalue+1)
        ans7=self.isValid(grid,row-1,col-2,n,expectedvalue+1)
        ans8=self.isValid(grid,row-2,col-1,n,expectedvalue+1)

        return ans1 or ans2 or ans3 or ans4 or ans5 or ans6 or ans7 or ans8

    def checkValidGrid(self, grid):
        n=len(grid)
        return self.isValid(grid,0,0,n,0)

## Time Complexity - O(8^(n^2))
## Recursion Stack Space Complexity - O(n^2-1)