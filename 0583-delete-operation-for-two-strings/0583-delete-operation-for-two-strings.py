class Solution(object):
    def SolveTab(self,word1,word2):
        M=len(word1)
        N=len(word2)
        dp=[[-1 for _ in range(N+1)]for _ in range(M+1)]

        # Handle Base Case:
        for j in range(N+1):
            dp[M][j]=N-j
        
        for i in range(M+1):
            dp[i][N]=M-i
        
        # Iterative approach: 
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                ans=0
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    ## Delete from the word1:
                    delete1=1 + dp[i+1][j]
                    ## Delete from the woed2:
                    delete2=1+dp[i][j+1]

                    dp[i][j]=min(delete1,delete2)

        return dp[0][0]


    def minDistance(self, word1, word2):
        return self.SolveTab(word1,word2)

## Time Complexity - O((M*N)) dp arraay each cell must be caluated single time
## Space Complexity - O(M*N) + O(M+N) Recusive Call stack depth
