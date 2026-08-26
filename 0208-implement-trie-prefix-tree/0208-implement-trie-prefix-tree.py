class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False
        
class Trie(object):
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        curr=self.root
        for ch in word:
            #convert each char into index
            index=ord(ch)-ord("a")
            #now check ch is already exists or not
            if curr.children[index] is None:
                #create a node
                curr.children[index]=TrieNode()
            curr=curr.children[index]
        curr.isEndOfWord=True 

    def search(self, word):
        curr=self.root
        for ch in word:
            index=ord(ch)-ord("a")
            if curr.children[index] is None:
                return False
            curr=curr.children[index]
        return curr.isEndOfWord
        
    def startsWith(self, prefix):
        curr=self.root
        for ch in prefix:
            index=ord(ch)-ord("a")
            if curr.children[index] is None:
                return False
            curr=curr.children[index]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)