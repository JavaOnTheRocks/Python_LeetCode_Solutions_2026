class Solution(object):
    def numRollsToTarget(self, n, k, target):
        #pahel ak colum ka liya
        #dp[row=dice][column=target]
        curr=[0 for _ in range(target+1)]
        prev=[0 for _ in range(target+1)]

        #Use Base Case
        prev[0]=1#current to count karenga na humap prev ha ussa 
        MOD = 10**9 + 7
        #apply iterative approach:
        for dice in range(1,n+1):
            for t in range(1,target+1):
                count = 0
                for i in range(1,k+1):#hama ak dice ka liya hi sara faces ka liya look out karna ha
                    if t-i>=0: 
                        count = (count + prev[t-i]) % MOD
                curr[t]=count
            #her iteration ak baad curr prev ho jayega
            prev=list(curr)
        return prev[target]

        