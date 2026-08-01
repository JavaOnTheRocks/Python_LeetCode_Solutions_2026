# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, target):
        newNode=TreeNode(target)

        if root is None:
            return newNode

        curr=root
        while curr is not None:
            if curr.val < target:
                if curr.right is None:
                    curr.right=newNode
                    break
                curr=curr.right
            else:
                if curr.left is None:
                    curr.left=newNode
                    break
                curr=curr.left
        return root 
# time complexity: O(h), Space coplexity: O(1)

        ## Recursive Appraoch
        # if root is None:
        #     return newNode
        # if root.val < target:
        #     root.right=self.insertIntoBST(root.right,target)
        # elif root.val > target:
        #     root.left=self.insertIntoBST(root.left,target)
        # return root
#Time complexity: O(h) , space coplexity:O(h)
        