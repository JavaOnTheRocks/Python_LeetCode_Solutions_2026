class Solution(object):
    def sortArray(self, nums):
        n=len(nums)
        #Base Case
        if len(nums)<=1:
            return nums

        start=0
        end=n-1
        mid = start + (end-start)//2

        left_half=nums[:mid+1]
        right_half=nums[mid+1:]

        left_sorted=self.sortArray(left_half)
        right_sorted=self.sortArray(right_half)

        return self.merge(left_sorted,right_sorted)

    def merge(self,left,right):
        sorted_nums=[]
        i=j=0
        while i < len(left) and j < len(right):
            if left[i]<right[j]:
                sorted_nums.append(left[i])
                i+=1
            else:
                sorted_nums.append(right[j])
                j+=1

        sorted_nums.extend(left[i:])
        sorted_nums.extend(right[j:])
        return sorted_nums
        
        

## Merge Sort Time Complexity - O(nlogn) and Space complexity - O(n)
        # n=len(nums)
        # for i in range(n):
        #     key=nums[i]
        #     j=i-1
        #     while nums[j]>key and j>=0:
        #         nums[j+1]=nums[j]
        #         j-=1
        #     nums[j+1]=key
        # return nums
## Insertion Sort with Wrost  case Time complexity - O(n^2) and Best case Time complexity - O(n)
#Space complexity O(1)

    # def sortArray(self, nums):
    #     n=len(nums)
    #     has_swapped=True
    #     while has_swapped:
    #         has_swapped=False
    #         for i in range(n-1):
    #             if nums[i]>nums[i+1]:
    #                 nums[i],nums[i+1]=nums[i+1],nums[i]
    #                 has_swapped=True
    #     return nums
#Bubble sort Wrost T.C. - O(n^2) Best T.C.- O(N)
#Space complexity - O(n)

        # n=len(nums)
        # for i in range(0,n):
        #     min_index=i
        #     for j in range(i+1, n):
        #         if nums[j]<nums[i]:
        #             min_index=j
        #     #swapping 
        #     nums[i],nums[min_index]=nums[min_index],nums[i]
        # return nums
#Time Complexity - o(n^2)  Require diffenet Sorting Algorithum.....
#Space complexity - o(1) in place modifiaction

        