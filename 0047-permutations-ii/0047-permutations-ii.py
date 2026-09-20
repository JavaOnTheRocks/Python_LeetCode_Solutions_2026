class Solution(object):
    def Recursionandbacktracking(self,nums,visited,ans,res):
        #Base Case
        if len(ans) == len(nums):
            res.append(list(ans))
            return
        
        for i in range(0,len(nums)):
            if not visited[i]:
                if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                    continue
                visited[i]=True
                ans.append(nums[i])
                self.Recursionandbacktracking(nums,visited,ans,res)
                #backtrack
                ans.pop()
                visited[i]=False
                
    def permuteUnique(self, nums):
        res=[]
        visited=[False]*len(nums)
        ans=[]
        nums.sort()#In place sorting
        #loop can handle finding element-
        self.Recursionandbacktracking(nums,visited,ans,res)
        return res
        