class Solution:
    def reverse(self, x: int) -> int:
        new_num=0
        num_str=str(x) if x > 0 else str(x)[1:]
        num_len=len(num_str)
        for i in range(num_len):
            new_num+= int(num_str[i])*pow(10,i)
        
        if new_num > pow(2,31)-1 or new_num < pow(-2,31):
            return 0
        
        if x < 0:
            new_num*=-1
        
        return new_num
