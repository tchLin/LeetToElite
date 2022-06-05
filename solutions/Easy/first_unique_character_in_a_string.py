class Solution:
    def firstUniqChar(self, s: str) -> int:
        check_dict={}
        for char in s:
            if char not in check_dict:
                check_dict[char] = 1
            else:
                check_dict[char] += 1
            
        for char in check_dict:
            if check_dict[char] == 1:
                return s.index(char)
        
        return -1
