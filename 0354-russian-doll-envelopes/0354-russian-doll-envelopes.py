class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        #applying Sorting 
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        
        #Now apply the LIS on the hight array:
        sub = []

        for env in envelopes:
            height=env[1]

            if len(sub)==0:
                sub.append(height)

            elif height > sub[-1]:
                sub.append(height)

            else:
                left=0
                right=len(sub)-1
                while left<=right:
                    mid=left + (right-left)//2

                    if sub[mid] >= height:
                        right=mid-1
                    else:
                        left=mid+1

                sub[left]=height

        return len(sub)

#appraoch using the Dp wiht BIary Search
# Time Complexity - O(nlogn)
# Space Complexity - O(n)

                







        
