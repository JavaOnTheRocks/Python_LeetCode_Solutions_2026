# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object): 
    def mirror(self,left,right):
        #Base Case
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        #recursive Case
        return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)


    def isSymmetric(self, root):
        if root is None:
            return True 
        #Recursive Solution
        return self.mirror(root.left,root.right)

        
        