class Solution(object):
    def Solve(self,matrix,i,j,dp):
        #Base Case
        if i>=len(matrix) or j>=len(matrix[0]):
            return 0
        
        if dp[i][j] != "-1":
            return dp[i][j]
            
        #Revursive Case
        right=self.Solve(matrix,i,j+1,dp)
        down=self.Solve(matrix,i+1,j,dp)
        diognal=self.Solve(matrix,i+1,j+1,dp)

        if matrix[i][j]=="1":
            dp[i][j]=1+min(right,down,diognal)
            self.final=max(self.final,dp[i][j])
            return dp[i][j]

        else: #add the Result into dp[i][j] then return
            dp[i][j]=0
            return 0

    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        #initallize 2d dp array:
        rows=len(matrix)
        cols=len(matrix[0])
        dp = [["-1" for _ in range(cols)] for _ in range(rows)]

        #initallize self as a global variable
        self.final=0
        self.Solve(matrix,0,0,dp)
        return self.final*self.final