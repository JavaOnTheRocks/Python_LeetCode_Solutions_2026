class TrieNode():
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False

class Solution(object):
    def __init__(self):
        self.root=TrieNode()
        self.ans=""

    def insert(self,word):
        curr=self.root
        for ch in word:
            index=ord(ch)-ord("a")
            if curr.children[index] is None:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
        curr.isEndOfWord = True

    def longestWord(self, words):
        for word in words:
            self.insert(word)
        self.ans=""
        temp=[]
        self.dfs(self.root,temp)
        return self.ans
    
    def dfs(self,node,temp):
        temp_word="".join(temp)

        # #base case
        # if node is None:
        #     return
        
        if len(temp_word)>len(self.ans):
            self.ans=temp_word
        
        #recursive case
        for i in range(26):
            child=node.children[i]
            if child is not None and child.isEndOfWord:
                temp.append(chr(i+ord("a")))
                
                self.dfs(child,temp)
                temp.pop()  # Backtrack       
        