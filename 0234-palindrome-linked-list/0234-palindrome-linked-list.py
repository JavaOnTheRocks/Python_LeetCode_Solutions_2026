# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head
        while fast!= None and fast.next:
            slow=slow.next
            fast=fast.next.next
        #Use three pointer to reverse the LinkedList:
        curr=slow
        prev=None
        nxt=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        left=head
        right=prev

        while right:
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True
        

        # #appraoch 1
        # curr=head
        # arr=[]
        # while curr != None:
        #     arr.append(curr.val)
        #     curr=curr.next
        # reverse_arr= arr[::-1]# with th help of slicing
        # return arr == reverse_arr
        # #time complexity = o(n)=o(n)+o(n)+o(n)
        # # space complexity = o(n)
