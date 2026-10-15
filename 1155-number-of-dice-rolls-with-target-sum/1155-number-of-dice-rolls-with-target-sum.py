class Solution(object):
    def numRollsToTarget(self, n, k, target):
        #pahel ak colum ka liya
        #dp[row=dice][column=target]
        dp=[[0 for _ in range(target+1)]for _ in range(n+1)]

        #Use Base Case
        dp[0][0]=1
        
        #apply iterative approach:
        for dice in range(1,n+1):
            for t in range(1,target+1):
                count = 0
                MOD = 10**9 + 7 
                for i in range(1,k+1):#hama ak dice ka liya hi sara faces ka liya look out karna ha
                    if t-i>=0: 
                        count = (count + dp[dice-1][t-i]) % MOD
                dp[dice][t]=count
        return dp[n][target]

        