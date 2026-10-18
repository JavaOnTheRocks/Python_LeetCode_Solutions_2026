class Solution(object):
    def minSwap(self, nums1, nums2):
        #List Concationation:
        nums1=[-1]+nums1
        nums2=[-1]+nums2
        n=len(nums1)
        #Two variable are changing (swapped,index)
        #dp=[[0 for _ in range(n+1)]for _ in range(2)]
        swap=0
        noswap=0
        currswap=0
        currnoswap=0
        #Base Case handle(alread uinitallized)
        # dp[0][n]=0
        # dp[1][n]=0

        #Apply iteraative appraoch:
        for index in range(n-1,0,-1):#Right to Left ja raha ha
            for swapped in range(1,-1,-1):
                ans=float("inf")
                #Recursive Case
                prev1=nums1[index-1]
                prev2=nums2[index-1]

                if swapped== 1:
                    prev1=nums2[index-1]
                    prev2=nums1[index-1]

                #No Swap(when strictely order ho)
                if nums1[index]>prev1 and nums2[index]>prev2:
                    # ans=min(ans,1+dp[0][index+1])
                    ans=min(ans,1+noswap)


                #Swap(when no strictely increasing order ho)
                if nums1[index]>prev2 and nums2[index]>prev1:
                    #ans=min(ans,dp[1][index+1])
                    ans=min(ans,swap)

                #dp[swapped][index]=ans
                if swapped==1:
                    currswap=ans
                else:
                    currnoswap=ans

            swap=currswap           
            noswap=currnoswap

        return noswap

#Time Complexity - O(N)
# Sapce Complexity - O(1)


        