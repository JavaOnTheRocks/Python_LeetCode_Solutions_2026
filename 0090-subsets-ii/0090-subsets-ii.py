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
        while index + 1 < len(nums) and nums[index]==nums[index+1]:
            index += 1
        self.helper(index+1,nums,curr_subset,res)
        
    def subsetsWithDup(self, nums):
        res=[]
        nums.sort()
        self.helper(0,nums,[],res)
        return res
        