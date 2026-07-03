# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getlen(self,head):
        l=0
        curr=head
        while curr.next!=None:
            curr=curr.next
            l+=1
        l+=1
        return l
    def getIntersectionNode(self, headA, headB):
        lenA=self.getlen(headA)
        lenB=self.getlen(headB)
        
        p1=headA
        p2=headB
        
        #align them
        if lenA>lenB:
            diff=lenA-lenB
            for i in range(diff):
                p1=p1.next
        else:
            diff=lenB-lenA
            for i in range(diff):
                p2=p2.next

        #move togather
        while p1 and p2:
            if p1==p2:
                return p1
            p1=p1.next
            p2=p2.next
        return None # No intersection 
        

        
        


        