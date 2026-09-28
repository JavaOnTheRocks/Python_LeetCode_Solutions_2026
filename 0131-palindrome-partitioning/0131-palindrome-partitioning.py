class Solution(object):
    def isPalindrome(self,s):
        clean_s=s.lower()
        return clean_s==clean_s[::-1]

    def getallPart(self,s,partition,ans):
        n=len(s)
        #Base Case
        if len(s)==0:
            ans.append(list(partition))#Copy of Partition
            return 
        
        for i in range(n):
            strpart=s[0:i+1]
            if (self.isPalindrome(strpart)):
                partition.append(strpart)
                #Recursive call for bacchi hui String:
                self.getallPart(s[i+1: ],partition,ans)
                #Backtrack Step
                partition.pop()


    def partition(self, s):
        ans=[]
        partition=[]
        self.getallPart(s,partition,ans)
        return ans


        