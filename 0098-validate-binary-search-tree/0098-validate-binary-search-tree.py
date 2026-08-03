# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,root, min, max):
        if root is None:
            return True
        if root.val<min or root.val>max:
            return False
        checkleft=self.check(root.left,min,root.val-1)
        checkright=self.check(root.right,root.val+1,max)
        return checkleft and checkright
    def isValidBST(self, root):
        left=float("-inf")
        right=float("inf")
        return self.check(root,left,right)

        