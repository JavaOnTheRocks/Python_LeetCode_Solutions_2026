class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class BrowserHistory(object):

    def __init__(self, homepage):
        #Home page to ak string ha to isa pahela Node ma convert karo
        self.current=Node(homepage)
        
    def visit(self, url):
        newNode=Node(url)
        self.current.next=None
        self.current.next=newNode
        newNode.prev=self.current
        self.current = newNode
        
        
    def back(self, steps):
        for i in range(steps):
            if self.current.prev is None:
                return self.current.val
            self.current=self.current.prev
        return self.current.val

    def forward(self, steps):
        for i in range(steps):
            if self.current.next is None:
                return self.current.val    
            self.current=self.current.next
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)