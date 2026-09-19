class Solution(object):
    def Recursionandbacktracking(self,nums,visited,ans,res):
        #Base Case
        if len(ans) == len(nums):
            res.append(list(ans))
            return
        
        for i in range(0,len(nums)):
            if not visited[i]:
                visited[i]=True
                ans.append(nums[i])
                self.Recursionandbacktracking(nums,visited,ans,res)
                #backtrack
                ans.pop()
                visited[i]=False
    def permute(self, nums):
        res=[]
        visited=[False]*len(nums)
        ans=[]
        #loop can handle finding element-
        self.Recursionandbacktracking(nums,visited,ans,res)
        return res
        