class Solution(object):
    def Solve(self,n,open_used,closed_used,current_str,ans):
        #Base Case
        if len(current_str)==2*n:
            ans.append(current_str)
            return #function backtrack from here and pop off the element form the recusive Stack
            
        #where we can use Closed 
        # 1. Explore the ')' path
        if open_used > closed_used:
            self.Solve(n,open_used,closed_used+1,current_str+")",ans)
        
        #Wen we can Use the Open 
        # 2. Explore the '(' path        
        if open_used < n:
            self.Solve(n,open_used+1,closed_used,current_str+"(",ans)


    def generateParenthesis(self, n):
        ans=[]
        self.Solve(n,0,0,"",ans)
        return ans
        

        