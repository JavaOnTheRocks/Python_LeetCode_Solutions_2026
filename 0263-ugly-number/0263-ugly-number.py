class Solution(object):
    def devideby(self,n,prime):
        while n % prime == 0:
            n=n//prime
        return n
    def isUgly(self, n):
        if n<=0:
            return False
        n=self.devideby(n,2)
        n=self.devideby(n,3)
        n=self.devideby(n,5)
        return n==1 #The remaining value itself tells you that another prime factor exists.