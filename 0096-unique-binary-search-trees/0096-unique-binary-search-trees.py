import math
class Solution(object):
    #Using Catlan Formula:
    def numTrees(self, n):
        upper = math.factorial(2 * n)
        lower = math.factorial(n+1) * math.factorial(n)
        return upper//lower

# time complexity - O(n)
# Space Complexity - O(1)


        
        