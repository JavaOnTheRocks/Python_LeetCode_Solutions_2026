class Solution(object):
    def SolveTab(self,text1,text2):
        m=len(text1)
        n=len(text2)

        curr_row=[0 for _ in range(n+1)]
        next_row=[0 for _ in range(n+1)]

        #Iterative Approach:
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (text1[i]==text2[j]):
                    curr_row[j]=1+ next_row[j+1]
                else:#not match the n i ko aaga badhao ya ja ko aaga badhao
                    curr_row[j]=max(next_row[j],curr_row[j+1])
            next_row=list(curr_row)

        return next_row[0]

    def longestCommonSubsequence(self, text1, text2):
        return self.SolveTab(text1,text2)

# TC - O(m*n) each cell computed only single time 
# SC - O(n) sapce, no recursive stack