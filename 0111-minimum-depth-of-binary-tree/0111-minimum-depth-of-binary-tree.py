# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        #base case
        if root is None:
            return 0
        
        #Recursive Case
        leftheight=self.minDepth(root.left)
        rightheight=self.minDepth(root.right)
        ans=min(leftheight,rightheight)+1
        if ans>1:
            return ans
        else:
            return max(leftheight,rightheight)+1
        