# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if root is None:
            return None
        #found then apply detetion
        if root.val==key:
            #at leaf no childern
            if root.left is None and root.right is None:
                return None
            #one childern 
            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            #Both childern are present
            else:
                temp = root.right
                while temp.left is not None:
                    temp=temp.left
                root.val=temp.val
                root.right=self.deleteNode(root.right,temp.val)


        # Search for the left side
        elif root.val > key:
            root.left=self.deleteNode(root.left,key)
        else:
            root.right=self.deleteNode(root.right,key)

        return root


        