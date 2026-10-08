class Solution(object):
    def SolveTab(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        #make an dp array
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)] #ewual to wali values automaticaly 0 initallize ho jaygi now

         
        #Base will be automatically filled:
        # convert Recursivley inot itratively with bottom up appraoach:
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                right=dp[i][j+1]
                down=dp[i+1][j]
                diognal=dp[i+1][j+1]

                if matrix[i][j]=="1":
                    dp[i][j]=1+min(right,down,diognal)
                    self.final=max(self.final,dp[i][j])
                    dp[i][j]

                else:
                    dp[i][j]=0


    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        
        self.final=0
        self.SolveTab(matrix)
        return self.final*self.final
