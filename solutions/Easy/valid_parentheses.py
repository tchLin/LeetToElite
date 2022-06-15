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
