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
    
    def SolveSC(self,word1,word2):
        M=len(word1)
        N=len(word2)

        curr_row=[-1 for _ in range(N+1)]
        next_row=[-1 for _ in range(N+1)]
        #Handle Base Case:
        for n in range(N+1):
            next_row[n]=N-n


        for i in range(M-1,-1,-1):
            #her ak row ka last wala col per 
            curr_row[N]=M-i
            for j in range(N-1,-1,-1):
                    #Recusive Case
                    if word1[i]==word2[j]:
                        curr_row[j]=next_row[j+1]
                    else:
                        ## insert:
                        insertAns=curr_row[j+1]

                        ## delete:
                        deleteAns=next_row[j]

                        ## replace:
                        replaceAns=next_row[j+1]

                        curr_row[j]=1 + min(insertAns,deleteAns,replaceAns)
            next_row=list(curr_row)             
        return next_row[0]

    def minDistance(self, word1, word2):
        return self.SolveSC(word1,word2)

## Time Complexity : O(M*n)
## Space Complexity - O(N)