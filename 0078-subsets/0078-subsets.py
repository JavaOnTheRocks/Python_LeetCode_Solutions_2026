class Solution(object):
    def helper(self,index,nums,curr_subset,res):
        #Base Case
        if index==len(nums):
            res.append(list(curr_subset))
            return
        #include
        curr_subset.append(nums[index])
        self.helper(index+1,nums,curr_subset,res)

        #exclude
        curr_subset.pop()
        self.helper(index+1,nums,curr_subset,res)

    def subsets(self, nums):
        res=[]
        self.helper(0,nums,[],res)
        return res
        