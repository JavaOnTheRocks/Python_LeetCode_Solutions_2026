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
        
        combination.append(arr[i])
        #Single include call:
        self.helper(arr,i+1,target-arr[i],combination,ans)

        #exclude call:
        combination.pop() #Backtrack Step

        next_index=i+1
        while next_index<n and arr[next_index]==arr[i]:
            next_index+=1

        self.helper(arr,next_index,target,combination,ans)


    def combinationSum2(self, candidates, target):
        n=len(candidates)
        ans=[]
        candidates.sort()
        #seen=set()# Beciuse we only ahve to Track the all unique combination
        self.helper(candidates,0,target,[],ans)
        return ans

        