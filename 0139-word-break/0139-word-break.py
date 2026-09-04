# Implemantation of TrieNode
class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        curr=self.root
        for ch in word:
            #convert each char into index
            index=ord(ch)-ord("a")
            #now check ch is already exists or not
            if curr.children[index] is None:
                #create a node
                curr.children[index]=TrieNode()
            curr=curr.children[index]
        curr.isEndOfWord=True #nikalta time true mark ker do

    def search(self,word):
        curr=self.root
        for ch in word:
            index=ord(ch)-ord("a")
            if curr.children[index] is None:
                return False
            curr=curr.children[index]
        return curr.isEndOfWord

    def startswith(self,prefix):
        curr=self.root
        for ch in prefix:
            index=ord(ch)-ord("a")
            if curr.children[index] is None:
                return False
            curr=curr.children[index]
        return True

class Solution(object):
    def wordBreak(self, s, wordDict):
        trie=Trie()
        for word in wordDict:
            trie.insert(word)
        # Memoization
        memo = {}
        #recursion call
        return self.solve(s,trie,memo)

    def solve(self, s, trie,memo):
    #Base case
        if len(s) == 0:
            return True
        if s in memo:
            return memo[s]
        for i in range(1, len(s) + 1):
            firstpart = s[0:i]
            remaining = s[i:]
            if trie.search(firstpart):
                if self.solve(remaining, trie,memo):
                    memo[s]=True
                    return True
        memo[s]=False
        return False
        
        