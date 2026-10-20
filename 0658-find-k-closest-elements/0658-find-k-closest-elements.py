class Solution(object):
    # Using Two Pointer Approach:
    def TwoPointer(self,arr,k,x):
        n=len(arr)
        start=0
        end=n-1
        
        #Keep Strinking
        # we are doin +1 becaouse we ahve to make index -1  because k len ka na ki indexes diff
        while end-start+1>k:
            dist_start = abs(arr[start] - x)
            dist_end = abs(arr[end] - x)

            if dist_start <= dist_end:
                end -= 1
            else:
                start+=1

        return arr[start:end+1]#Slicing m last wal element include nhi hota

## Time Complexity - O(n)
## Space Complexty _ O(1)

    def findClosestElements(self, arr, k, x):
        return self.TwoPointer(arr,k,x)




        