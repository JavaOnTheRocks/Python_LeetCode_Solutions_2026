class Solution(object):
    def Solve(self,text1,text2,i,j,dp):
        #Base Case
        if i >= len(text1):
            return 0

        if j >= len(text2):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        #Recursive Case
        #If char match:
        if (text1[i]==text2[j]):
            dp[i][j]=1+self.Solve(text1,text2,i+1,j+1,dp)
        else:#not match the n i ko aaga badhao ya ja ko aaga badhao
            dp[i][j]=max(self.Solve(text1,text2,i+1,j,dp),self.Solve(text1,text2,i,j+1,dp))

        return dp[i][j]

    def longestPalindromeSubseq(self, s):
        rev_s=s[::-1]
        m=len(s)
        n=len(rev_s)
        dp=[[-1 for _ in range(n+1)]for _ in range(m+1)]
        return self.Solve(s,rev_s,0,0,dp)

## Time Complexity - Exponantial- O((m*n)) each cell must be computed single time 
## Space Complexity - O(m*n) extra space + O(m+n) Recusive approach
        