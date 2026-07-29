# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.balanced=True
    def height(self,root):
        if root is None:
            return 0
        
        leftheight=self.height(root.left)
        rightheight=self.height(root.right)
        #Ager kisi bhi point pa height differene 1 sa jayada ha
        if abs(leftheight-rightheight)>1:
            self.balanced=False
        
        return max(leftheight,rightheight)+1

    def isBalanced(self, root):
        self.height(root)#isma pahala ya run hona chiya output yahi to dega
        return self.balanced


        
        