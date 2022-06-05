class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        replace_pointer=1
        temp = nums[0]
        for i in range(len(nums)):
            if temp != nums[i]:
                nums[replace_pointer] = temp = nums[i]
                replace_pointer+=1
        
        return replace_pointer
