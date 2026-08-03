# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count=0
        self.result=0
    def inorder(self,root,k):
        #Base case
        if root is None:
            return

        self.inorder(root.left,k) 

        self.count+=1
        if self.count == k:
            self.result=root.val
            return

        self.inorder(root.right,k)

    def kthSmallest(self, root, k):
        self.inorder(root,k)
        return self.result
    ## Appraoch 1

    # def __init__(self):
    #     self.ans=[]
    # def inorder(self,root):
    #     #Base case
    #     if root is None:
    #         return
    #     self.inorder(root.left) 
    #     self.ans.append(root.val)
    #     self.inorder(root.right)
    # def kthSmallest(self, root, k):
    #     self.inorder(root)
    #     return self.ans[k-1] # k-1 th index
    # ## Time and Space complexity of this code is o(n) ,o(n)
    

        


        