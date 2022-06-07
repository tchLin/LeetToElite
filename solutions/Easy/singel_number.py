#Xor compares two binary numbers bitwise
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for num in nums:
            xor^=num
        return xor



#slower solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=sum(set(nums))*2
        return num-sum(nums)
