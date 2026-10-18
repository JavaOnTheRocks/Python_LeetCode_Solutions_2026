class Solution(object):
    #Find The Longest Length of AP:
    def longestArithSeqLength(self, nums):
        n=len(nums)
        #Base Case:
        if n<= 2:
            return n

        dp=[{} for _ in range(n)]

        ans=0
        for i in range(1,n):
            for j in range(0,i):
                diff=nums[i]-nums[j]
                if diff in dp[j]:
                    dp[i][diff]=1+dp[j][diff]
                else:
                    dp[i][diff]=2
                ans=max(ans,dp[i][diff])
                # #Backword lookup logic 
                # ans=max(ans,2+self.Solve(i,nums[j]-nums[i],nums,dp))
        return ans

#TIme Complexity = O(n^2)
#Space Complexity = O(n^2)


        