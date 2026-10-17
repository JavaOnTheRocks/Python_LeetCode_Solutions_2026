class Solution(object):
    def Solve(self,nums1,nums2,index,swapped,dp):
        #Base Case
        if index==len(nums1):
            return 0
        
        prev1=nums1[index-1]
        prev2=nums2[index-1]

        if swapped== 1:
            prev1=nums2[index-1]
            prev2=nums1[index-1]
        
        if dp[swapped][index] != -1:
            return dp[swapped][index]
        
        ans=float("inf")
        #Recursive Case
        
        #No Swap(when strictely order ho)
        if nums1[index]>prev1 and nums2[index]>prev2:
            ans=min(ans,1+self.Solve(nums1,nums2,index+1,0,dp))


        #Swap(when no strictely increasing order ho)
        if nums1[index]>prev2 and nums2[index]>prev1:
            ans=min(ans,self.Solve(nums1,nums2,index+1,1,dp))

        dp[swapped][index]=ans
        return dp[swapped][index]

    def minSwap(self, nums1, nums2):
        n=len(nums1)
        #List Concationation:
        nums1=[-1]+nums1
        nums2=[-1]+nums2
        #Two variable are changing (swapped,index)
        dp=[[-1 for _ in range(n+1)]for _ in range(2)]
        return self.Solve(nums1,nums2,1,0,dp)

        