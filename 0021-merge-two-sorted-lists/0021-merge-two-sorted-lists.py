# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        curr1=list1
        curr2=list2
        dummy=ListNode(0)
        curr=dummy

        while curr1 != None and curr2 != None:
            if curr1.val<=curr2.val:
                curr.next=curr1
                curr=curr.next
                curr1=curr1.next
            else:
                curr.next=curr2
                curr=curr.next
                curr2=curr2.next
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2
        return dummy.next

           