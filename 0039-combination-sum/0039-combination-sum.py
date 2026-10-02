class Solution(object):
    def helper(self,arr,i,target,combination,ans):
        n=len(arr)
        #Base Case
        if target==0:
            ans.append(list(combination))
            return
        
        if target<0:
            return
        if i==n:
            return
        
        #Recursive Case
        combination.append(arr[i])
        #Single Include call
        # self.helper(arr,i+1,target-arr[i],combination,ans,seen)
        #Multiple include Call
        self.helper(arr,i,target-arr[i],combination,ans)

        #Exclude call
        combination.pop() #Backtrack Step
        self.helper(arr,i+1,target,combination,ans)

    def combinationSum(self, candidates, target):
        n=len(candidates)
        ans=[]
        #seen=set()# Beciuse we only ahve to Track the all unique combination
        self.helper(candidates,0,target,[],ans)
        return ans

## WE Dont need Single Include it will hangle already and also handle the duplicate automatically

        