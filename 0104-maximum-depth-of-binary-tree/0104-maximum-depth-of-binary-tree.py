# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        #Base Case
        if root==None:
            return 0
        #Recursive Case
        leftheight=self.maxDepth(root.left)
        rightheight=self.maxDepth(root.right)
        return max(leftheight,rightheight)+1
        