class Solution(object):
    def SolveSO(self,text1,text2):
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
            next_row=list(curr_row) #Creating an copy insted of point reference

        return next_row[0]



    def longestPalindromeSubseq(self, s):
        rev_s=s[::-1]
        return self.SolveSO(s,rev_s)

## Time Complexity - Exponantial- O((m*n)) each cell must be computed single time 
## Space Complexity - O(m*n) extra space 
        