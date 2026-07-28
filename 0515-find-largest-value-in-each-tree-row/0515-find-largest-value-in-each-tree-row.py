# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count=0 #size count karna ka liya 

    #Insert Element at rear:
    def enqueue(self,data):
        newNode=Node(data)
        if self.front is None:
            self.front=newNode
            self.rear=newNode
            self.count+=1
            return
        self.rear.next=newNode
        self.rear=newNode
        self.count+=1
    
    #Remove From Front:
    def dequeue(self):
        if self.front is None:
            return None
        removed=self.front.data
        self.front=self.front.next
        self.count-=1
        return removed
    
    #Return From Front:
    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def size(self):
        if self.front is None:
            return 0

        return self.count
    
    #Check is Empty:
    def isEmpty(self):
        return self.front is None

class Solution(object):
    def largestValues(self, root):
        queue=Queue()

        if root is None:
            return []

        ans=[]
        ans.append(root.val)
        queue.enqueue(root)

        while queue.size()>0:
            l=queue.size()
            level=[]
            for i in range(l):
                front=queue.dequeue()
                if front.left != None:
                    level.append(front.left.val)
                    queue.enqueue(front.left)
                if front.right != None:
                    level.append(front.right.val)
                    queue.enqueue(front.right)
            if len(level)>0:
                ans.append(max(level))
        return ans

        
        
        