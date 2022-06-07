class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevtable={}
        for i, num in enumerate(nums):
            key = target - num
            if key in prevtable:
                return [prevtable[key], i]
            prevtable[num] = i
