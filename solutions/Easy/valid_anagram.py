# less memory # faster
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        s_len=len(s)
        t_len=len(t)
        # if lengths for both string are different
        if s_len != t_len:
            return False
        # keep track of char count for both string using dict
        for s_char, t_char in zip(s, t):
            s_dict[s_char]=s_dict.get(s_char, 0)+1
            t_dict[t_char]=t_dict.get(t_char, 0)+1
        
        # check edge cases i.e s='abc' t='bcat'
        for char in s_dict:
            t_dict[char]=t_dict.get(char, 0)
            if s_dict[char] != t_dict[char]:
                return False
        for char in t_dict:
            s_dict[char]=s_dict.get(char, 0) 
            if t_dict[char] != s_dict[char]:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return (sorted(list(s))) == (sorted(list(t)))
