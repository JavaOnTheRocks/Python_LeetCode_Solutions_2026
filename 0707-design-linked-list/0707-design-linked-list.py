class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index):
        #Index validation 
        if index<0 or index>self.size-1:
            return -1
        curr=self.head
        for i in range(index):
            curr=curr.next
        return curr.val

        
        

    def addAtHead(self, val):
        newNode=Node(val)
        #connr=ect to new Node
        newNode.next=self.head
        #Move the head (beous yaha head banega naya)
        self.head=newNode
        self.size+=1

    def addAtTail(self, val):
        newNode=Node(val)
        curr=self.head
        if curr is None:
            # newNode.next=self.head
            self.head=newNode
            self.size+=1
            return
        while curr.next!=None:
            curr=curr.next
        curr.next=newNode
        self.size+=1


    def addAtIndex(self, index, val):
        if index==0:
            self.addAtHead(val)
            return
        if index==self.size:
            self.addAtTail(val)
            return
        if index > self.size:
            return 
        if index<0:
            index=0

        newNode=Node(val)
        curr=self.head 
        for i in range(index-1):
            curr=curr.next
        newNode.next=curr.next
        curr.next=newNode
        self.size+=1

    def deleteAtIndex(self, index):
        #edge cases
        if index<0 or index>=self.size:
            return
        if index==0:
            self.head=self.head.next
            self.size-=1
            return
        curr=self.head
        for i in range(index-1):
            curr=curr.next
        curr.next=curr.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)