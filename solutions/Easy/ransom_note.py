class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict={}
        for i in magazine:
            mag_dict[i]=mag_dict.get(i, 0)+1
            
        ranm_dict={}
        for i in ransomNote:
            ranm_dict[i]=ranm_dict.get(i, 0)+1
        
        for i in ranm_dict:
            mag_dict[i]=mag_dict.get(i,0)
            if not ranm_dict[i] <= mag_dict[i]:
                return False
        return True
