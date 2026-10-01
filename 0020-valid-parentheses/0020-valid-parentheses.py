class Solution(object):
    def isValid(self, s):
        stack=[]
        for ch in s:
            #add opening brackets to the stack
            if(ch=="(" or ch=="[" or ch =="{"):
                stack.append(ch)
            else:#closing
                if (len(stack)==0):
                    return False
                    
                if((ch==")" and stack[-1]=="(") or (ch=="]" and stack[-1]=="[") or (ch=="}" and stack[-1]=="{")):
                    stack.pop()
                else:
                    return False

        return len(stack)==0
        # n=len(s)
        # for i in range(n):
        #     stack.append(s[i])
        # return stack
        