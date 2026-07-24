# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #Helper Function
    def preorder(self, root):
        # Base case
        if root is None:
            return
        # Recursive case
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root):
        self.ans=[]
        self.preorder(root)
        return self.ans

        


        