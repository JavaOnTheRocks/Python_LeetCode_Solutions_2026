# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, head1, head2):
        curr1=head1
        curr2=head2
        dummy=ListNode(0)
        curr=dummy
        carry=0

        while curr1 or curr2 or carry:
            if curr1:
                x=curr1.val
            else:
                x=0
            if curr2:
                y=curr2.val
            else:
                y=0
            total = x + y + carry
            digit = total % 10
            carry = total // 10
            curr.next=ListNode(digit)
            curr=curr.next
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        return dummy.next




        # l1=0
        # l2=0    
        # while curr1.next != None:
        #     curr1=curr1.next
        #     l1+=1
        # l1+1
        # while curr2.next != None:
        #     curr2=curr2.next
        #     l2+=2
        # l2+1
        # if l2>l1:
        #     diff=l2-l1
        #     for i in range(diff):
        #         curr1.next=ListNode(0)
        #         curr1=curr1.next
        # else:
        #     diff=l1-l2
        #     for i in range(diff):
        #         curr2.next=ListNode(0)
        #         curr2=curr2.next
        # # Create a new Linked List:
        # dummy=ListNode(0)
        # head=dummy

        # while curr1 or curr2:


        

        