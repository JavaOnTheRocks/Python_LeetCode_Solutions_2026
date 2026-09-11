class Solution(object):
    #Recusion in this function
    #We are not making the dp a attribute of this class so we are passing the dp in solve function,we can make a attribute using self.
    def solve(self,n,dp):
        #Base case
        if n == 0 or n==1:
            return n
        
        if dp[n]!=-1:
            return dp[n]
        

        dp[n]=self.solve(n-1,dp) + self.solve(n-2,dp)
        return dp[n]

    #def solve(n)
    def fib(self, n):
        dp=[-1]*(n+1)
        
        return self.solve(n,dp)

#__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))