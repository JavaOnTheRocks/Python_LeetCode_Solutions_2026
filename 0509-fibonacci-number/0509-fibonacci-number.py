class Solution(object):
    #with tabulization
    def fib(self, n):
        if n <= 1:
            return n
        
        prev2=0
        prev1=1

        for i in range(2,n+1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr

        return prev1

#__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))