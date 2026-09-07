# Implementation of TrieNode
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
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        trie=Trie()
        for word in strs:
            trie.insert(word)

        prefix=[]
        node=trie.root
        while True:
            index = -1
            count = 0
            for i in range(26):
                if node.children[i] is not None:
                    count += 1
                    index = i
            if count != 1 or node.isEndOfWord:
                break
            char=chr(index+ord("a"))
            prefix.append(char)
            node=node.children[index]

        return "".join(prefix)


        
        