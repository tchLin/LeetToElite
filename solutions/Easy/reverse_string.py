class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half=floor(len(s)/2)
        for x in range(half):
            s[x], s[len(s)-x-1] = s[len(s)-x-1], s[x] 
            
