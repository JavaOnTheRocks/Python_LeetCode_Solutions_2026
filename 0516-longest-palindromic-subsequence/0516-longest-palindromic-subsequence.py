class Solution(object):
    def SolveTab(self,text1,text2):
        m=len(text1)
        n=len(text2)
        dp=[[0 for _ in range(n+1)]for _ in range(m+1)]

        #Iterative Approach:
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (text1[i]==text2[j]):
                    dp[i][j]=1+ dp[i+1][j+1]
                else:#not match the n i ko aaga badhao ya ja ko aaga badhao
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])

        return dp[0][0]


    def longestPalindromeSubseq(self, s):
        rev_s=s[::-1]
        return self.SolveTab(s,rev_s)

## Time Complexity - Exponantial- O((m*n)) each cell must be computed single time 
## Space Complexity - O(m*n) extra space 
        