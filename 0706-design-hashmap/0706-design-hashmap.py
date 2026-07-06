class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None

class MyHashMap(object):

    def __init__(self):
        self.size=1000
        self.hashtable=[None]*self.size
        

    def hashfunction(self,key):
        index = key % self.size #self.key now variable in this class
        return index

    def put(self, key, value):
        index =self.hashfunction(key)

        head=self.hashtable[index]

        newNode=Node(key,value)
        if head==None:
            self.hashtable[index]=newNode
            return
        #Travese the linked list 
        curr=head
        while curr:
            if curr.key==key:
                #update value 
                curr.val=value
                return
            if curr.next is None:
                break
            curr=curr.next
        curr.next=newNode
                
    def get(self, key):
        index=self.hashfunction(key)
        head=self.hashtable[index]
        curr=head
        while curr:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1
        

    def remove(self, key):
        index=self.hashfunction(key)
        head=self.hashtable[index]
        prev=None
        curr=head
        while curr:
            if curr.key==key:
                if prev==None:
                    self.hashtable[index]=curr.next
                else:
                    prev.next=curr.next
            prev=curr
            curr=curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)