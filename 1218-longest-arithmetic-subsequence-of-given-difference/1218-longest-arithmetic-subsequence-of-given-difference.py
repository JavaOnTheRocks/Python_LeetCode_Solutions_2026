class Solution(object):
    #Brute Force Appraoch:
    def longestSubsequence(self, arr, difference):
        n=len(arr)
        if n==0:
            return 0
        dp={}
        ans=0
        for num in arr:
            temp=num-difference
            if temp in dp:
                dp[num]=dp[temp]+1
            else:
                dp[num]=1#Store in Key Value Pair
            ans=max(ans,dp[num])
        return ans

## Time Complexity _ O(n)
## Sapce Complexity _ O(n)


