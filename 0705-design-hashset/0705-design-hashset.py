class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
class MyHashSet(object):

    def __init__(self):
        self.size=1000
        self.hashtable=[None]*self.size
    
    def hashfunction(self,key):
        index = key % self.size
        return index

    def add(self, key):
        index=self.hashfunction(key)
        head=self.hashtable[index]
        newNode=Node(key)
        #if the index array in empty
        if head==None:
            self.hashtable[index]=newNode
            return
        # add with traversal
        curr=head
        while curr:
            #update and at the end
            if curr.key==key:
                return
            if curr.next==None:
                break
            curr=curr.next
        curr.next=newNode
        

    def remove(self, key):
        index=self.hashfunction(key)
        head=self.hashtable[index]
        prev=None
        curr=head
        while curr:
            if curr.key==key:
                #at first
                if prev is None:
                    self.hashtable[index]=curr.next
                else:
                    prev.next=curr.next
                return 
            prev=curr
            curr=curr.next


    def contains(self, key):
        index=self.hashfunction(key)
        head=self.hashtable[index]
        curr=head
        while curr:
            if curr.key==key:
                return True
            curr=curr.next
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)