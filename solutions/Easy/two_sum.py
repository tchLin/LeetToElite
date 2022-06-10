class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        for i, num in enumerate(nums):
            if target-num in num_dict:
                return [num_dict[target-num], i]
            num_dict[num]=num_dict.get(num, i)
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevtable={}
        for i, num in enumerate(nums):
            key = target - num
            if key in prevtable:
                return [prevtable[key], i]
            prevtable[num] = i
