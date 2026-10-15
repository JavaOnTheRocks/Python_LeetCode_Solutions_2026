class Solution(object):
    def Solve(self,dice,faces,target,dp):
        #Base Case
        if target<0:
            return 0
        if dice==0 and target != 0:
            return 0
        if target==0 and dice != 0:
            return 0 #kabhi ban hianhi payenga 0 np wayes
        if target==0 and dice==0:
            return 1
            #only one way kuch hi mut karo
        
        #if pahela hi calculate ker liya ha to
        if dp[dice][target] != -1:
            return dp[dice][target]

        #Recursive Case
        #Sequentially Traversal
        count = 0
        MOD = 10**9 + 7 
        for i in range(1,faces+1):
            count = (count + self.Solve(dice-1,faces,target-i,dp)) % MOD
            
        dp[dice][target]=count
        return dp[dice][target]#yaha hum dice n ka liya nikala ki kosish ker raha ha.

    def numRollsToTarget(self, n, k, target):
        #pahel ak colum ka liya
        #dp[row=dice][column=target]
        dp=[[-1 for _ in range(target+1)]for _ in range(n+1)]
        return self.Solve(n,k,target,dp)

        