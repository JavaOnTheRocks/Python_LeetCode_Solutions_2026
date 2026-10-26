class Solution(object):
    def Solve(self,word1,word2,i,j,dp):
        #Base Case
        if i==len(word1):
            return len(word2)-j#itna insert operation honga word2 ko word 1 jesa banana ma
        
        if j==len(word2):
            return len(word1)-i#itna delted operation honga word 1 ko word 2 jesa banana ma
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        #Recusive Case
        ans=0
        if word1[i]==word2[j]:
            return self.Solve(word1,word2,i+1,j+1,dp)
        else:
            ## insert:
            insertAns=1 + self.Solve(word1,word2,i,j+1,dp)#cure operation and aagan wala ka liya recursive call

            ## delete:
            deleteAns=1 + self.Solve(word1,word2,i+1,j,dp)

            ## replace:
            replaceAns=1 + self.Solve(word1,word2,i+1,j+1,dp)

            ans=min(insertAns,deleteAns,replaceAns)

        dp[i][j]=ans
        return dp[i][j]

    def minDistance(self, word1, word2):
        M=len(word1)
        N=len(word2)
        #two varubale are chnaging so that 2d dp
        dp=[[-1 for _ in range(N+1)]for _ in range(M+1)]
        return self.Solve(word1,word2,0,0,dp)

        