class Solution(object):
    def helper(self,nums,index,target,combination,ans,k):
        n=len(nums)
        #Base Cases
        if target == 0:
            if len(combination)==k:
                ans.append(list(combination))
            return 
        if target < 0:
            return 
        if index == n:
            return 
        if len(combination)>k:
            return

        #Recursive Case
        combination.append(nums[index])
        #Include Multiple item
        self.helper(nums,index+1,target-nums[index],combination,ans,k)
        
        #BackTrack Step
        combination.pop()
        #Exclude item
        self.helper(nums,index+1,target,combination,ans,k)


    def solve(self,nums,target,k):
        n=len(nums)
        ans=[]
        self.helper(nums,0,target,[],ans,k)
        return ans

    def combinationSum3(self, k, n):
        nums=[1,2,3,4,5,6,7,8,9]
        return self.solve(nums,n,k)
    

        