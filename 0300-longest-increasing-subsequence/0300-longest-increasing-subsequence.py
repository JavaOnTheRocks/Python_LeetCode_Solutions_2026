class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        if n==0:
            return 0
        ans=[]
        ans.append(nums[0])

        for num in nums:
            if num > ans[-1]:
                ans.append(num)
            else:
                left=0
                right=len(ans)-1

                while left<=right:
                    mid=left+(right-left)//2

                    if ans[mid]>=num:
                        right = mid-1
                    else:
                        left=mid+1

                ans[left]=num
        return len(ans)


