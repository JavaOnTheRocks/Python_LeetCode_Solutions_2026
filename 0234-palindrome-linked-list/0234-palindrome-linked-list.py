# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        #appraoch 1
        curr=head
        arr=[]
        while curr != None:
            arr.append(curr.val)
            curr=curr.next
        reverse_arr= arr[::-1]# with th help of slicing
        return arr == reverse_arr
        #time complexity = o(n)=o(n)+o(n)+o(n)
        # space complexity = o(n)
