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

        if root.left == None:
            return rightheight+1
        if root.right == None:
            return leftheight+1
        else:
            return min(leftheight,rightheight)+1
        