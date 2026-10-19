class Solution(object):
    #Tabulization(Bottom - up) Appraoch:
    def numTrees(self, n):
        dp=[0 for _ in range(n+1)]

        #Convert Base Case
        dp[0]=dp[1]=1

        # Build the table bottom-up from 2 up to n
        for i in range(2,n+1):#Insted of calling Solve(n)
            for j in range(1,i+1):#picing the root node 
                dp[i]+=dp[j-1]*dp[i-j]
    
        return dp[n]

## Tabulization appraoch:

## Time Cmplexity - Exponential - O(n^2)
## Sapce Complexity - O(n) 
# No Recusive dpeth Exced erro remove the Recusion from the game (avoid Stack Frame Allocation)
        
        