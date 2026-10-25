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

    def longestCommonSubsequence(self, text1, text2):
        m=len(text1)
        n=len(text2)
        dp=[[-1 for _ in range(n+1)]for _ in range(m+1)]
        #Kisi bhi char ko inclde or Exclude ker sakta ha so that apply Recursion:
        return self.Solve(text1,text2,0,0,dp)

# TC - O(2^(m+n))
# SC - O(m+n) Recursive Staack