class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False

class WordDictionary(object):
    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word):
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
        def dfs(word_index,node):
            #base case
            if word_index == len(word):
                return node.isEndOfWord

            #Recursive case
            char=word[word_index]
            if char == ".":
                for child in node.children:
                    if child is not None:
                        if dfs(word_index+1,child):
                            return True
                return False
            else:
                index=ord(char)-ord("a")
                if node.children[index] is None:
                    return False
                return dfs(word_index+1,node.children[index])
        return dfs(0,self.root)


## In Normal Condition:
    # def search(self, word):
    #     curr=self.root
    #     for ch in word:
    #         index=ord(ch)-ord("a")
    #         if curr.children[index] is None:
    #             return False
    #         curr=curr.children[index]
    #     return curr.isEndOfWord
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)