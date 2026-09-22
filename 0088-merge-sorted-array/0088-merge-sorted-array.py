class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=m-1
        j=n-1
        k=m+n-1

        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                #picha sa isliya dalna suru ker rah ha becous ispa hum array 1 ko overwrite na ker raha ho or bigger element ko picha append ker saka
                nums1[k]=nums1[i]
                i-=1
                k-=1
            else:
                nums1[k]=nums2[j]
                j-=1
                k-=1
        while j>=0:
            nums1[k]=nums2[j]
            k-=1
            j-=1



                



        