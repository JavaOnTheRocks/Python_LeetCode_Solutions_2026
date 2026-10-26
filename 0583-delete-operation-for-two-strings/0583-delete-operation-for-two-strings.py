class Solution(object):
    def SolveMem(self,word1,word2,i,j,dp):
        #Base Case:
        #If we reach end of the word1 then delete all the reamaining char from word2
        if i == len(word1):
            return len(word2)-j
        
        #IF we reach end of the word2 then delete all the remaining char from word1
        if j == len(word2):
            return len(word1)-i
        
        if dp[i][j] != -1:
            return dp[i][j]

        #Recusive Appraoch:
        ans=0
        if word1[i]==word2[j]:
            dp[i][j]=self.SolveMem(word1,word2,i+1,j+1,dp)
        else:
            ## Delete from the word1:
            delete1=1 + self.SolveMem(word1,word2,i+1,j,dp)
            ## Delete from the woed2:
            delete2=1+self.SolveMem(word1,word2,i,j+1,dp)

            dp[i][j]=min(delete1,delete2)

        return dp[i][j]

    def minDistance(self, word1, word2):
        M=len(word1)
        N=len(word2)
        dp=[[-1 for _ in range(N+1)]for _ in range(M+1)]
        return self.SolveMem(word1,word2,0,0,dp)

## Time Complexity - O((M*N)) dp arraay each cell must be caluated single time
## Space Complexity - O(M*N) + O(M+N) Recusive Call stack depth
