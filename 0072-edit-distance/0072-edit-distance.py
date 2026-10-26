class Solution(object):
    def SolveTab(self,word1,word2):
        M=len(word1)
        N=len(word2)

        dp=[[-1 for _ in range(N+1)]for _ in range(M+1)]
        #Handle Base Case:
        for n in range(N+1):
            dp[M][n]=N-n
        
        for m in range(M+1):
            dp[m][N]=M-m

        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                    #Recusive Case
                    if word1[i]==word2[j]:
                        dp[i][j]=dp[i+1][j+1]
                    else:
                        ## insert:
                        insertAns=dp[i][j+1]

                        ## delete:
                        deleteAns=dp[i+1][j]

                        ## replace:
                        replaceAns=dp[i+1][j+1]

                        dp[i][j]=1 + min(insertAns,deleteAns,replaceAns)
                        
        return dp[0][0]

    def minDistance(self, word1, word2):
        return self.SolveTab(word1,word2)

        