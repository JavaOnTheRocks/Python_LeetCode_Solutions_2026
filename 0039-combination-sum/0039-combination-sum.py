class Solution(object):
    def helper(self,arr,i,target,combination,ans,seen):
        n=len(arr)
        #Base Case
        if target==0:
            touple_combination=tuple(combination)
            if touple_combination not in seen:
                seen.add(touple_combination)
                ans.append(list(combination))
            return
        
        if target<0:
            return
        if i==n:
            return
        
        #Recursive Case
        combination.append(arr[i])
        #Single Include call
        self.helper(arr,i+1,target-arr[i],combination,ans,seen)
        #Multiple include Call
        self.helper(arr,i,target-arr[i],combination,ans,seen)

        #Exclude call
        combination.pop() #Backtrack Step
        self.helper(arr,i+1,target,combination,ans,seen)

    def combinationSum(self, candidates, target):
        n=len(candidates)
        ans=[]
        seen=set()
        self.helper(candidates,0,target,[],ans,seen)
        return ans

        