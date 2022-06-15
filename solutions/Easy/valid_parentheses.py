class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        lookup={"}":"{", "]":"[", ")":"("}
        for brac in s:
            if brac in lookup:
                if not stack or stack.pop()!=lookup[brac]:
                    return False
            else:
                stack.append(brac)
            
        return True if not stack else False
    
class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        for brac in s:
            if (brac == "{" or brac == "[" or brac == "("):
                li.append(brac)
            
            if (brac == "}" or brac == "]" or brac == ")") and len(li)==0:
                return False
    
            if brac == "]" and li[-1] != "[":
                return False
            elif brac == "}" and li[-1] != "{":
                return False
            elif brac == ")" and li[-1] != "(":
                return False
            
            if brac == "]" and li[-1] == "[":
                li.pop()
            elif brac == "}" and li[-1] == "{":
                li.pop()
            elif brac == ")" and li[-1] == "(":
                li.pop()
        
        return False if len(li)>0 else True
