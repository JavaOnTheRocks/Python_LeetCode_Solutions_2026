# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while curr and curr.next:
            #duplicate available 
            if curr.val == curr.next.val:
                x=curr.val
                while curr and curr.val==x:
                    curr=curr.next
                prev.next=curr
            #Not available
            else:
                prev=curr
                curr=curr.next
        return dummy.next

       
        
        