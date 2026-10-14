class Solution(object):
    def check(self,base,newbox):
        if newbox[0]<=base[0] and newbox[1]<=base[1] and newbox[2] <= base[2]:
            return True
        else:
            return False

    def heightOfLIS(self, nums):
        n=len(nums)
        currRow=[0 for _ in range(n+1)]
        nextRow=[0 for _ in range(n+1)]
        #Base Case witll me hangeseld automatically becous we intallized 0 inatially.
        #for prev in range(0,n+1):
        #dp[n][prev]=0

        #Convert Rcursive in iterative approach:
        for curr in range(n-1,-1,-1):
            for prev in range(n-1,-2,-1):
                take=0 #Takki error na aaya
                if prev==-1 or self.check(nums[curr],nums[prev]):#Yah hum prev box ko curr box pa rukhan ha rah ah yah huma nested for loop baa raha ha
                    take+=nums[curr][2]+nextRow[curr+1]

                #Exclude Case
                notake=0+ nextRow[prev+1]#dp wala array ma sara m aprev+1 karna pud jayega

                currRow[prev+1]=max(take,notake)
            nextRow=list(currRow)
        return nextRow[0]

    def maxHeight(self, cuboids):
        for c in cuboids:
            c.sort()
        #Sort all cuboid on the basis of weidthe or length
        cuboids.sort()

        #Use LIS ka logic
        return self.heightOfLIS(cuboids)

