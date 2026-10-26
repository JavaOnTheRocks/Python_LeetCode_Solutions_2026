class Solution(object):
    def SolveSO(self,word1,word2):
        M=len(word1)
        N=len(word2)
        curr_row=[-1 for _ in range(N+1)]
        next_row=[-1 for _ in range(N+1)]

        # Handle Base Case:
        for j in range(N+1):
            next_row[j]=N-j
        
        # for i in range(M+1):
        #     dp[i][N]=M-i
        
        # Iterative approach:(isma curent caluculate kareanga) 
        for i in range(M-1,-1,-1):
            #Base Case her ak row ka end wal ma yaha rukhna ha
            curr_row[N]=M-i
            for j in range(N-1,-1,-1):
                if word1[i]==word2[j]:
                    curr_row[j]=next_row[j+1]
                else:
                    ## Delete from the word1:
                    delete1=1 + next_row[j]
                    ## Delete from the woed2:
                    delete2=1+curr_row[j+1]

                    curr_row[j]=min(delete1,delete2)

            next_row=list(curr_row)
        return next_row[0]


    def minDistance(self, word1, word2):
        return self.SolveSO(word1,word2)

## Time Complexity - O((M*N)) dp arraay each cell must be caluated single time
## Space Complexity - O(N)
