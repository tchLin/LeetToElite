class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict={}
        li=[]
        for num in nums1:
            dict[num]=dict.get(num, 0)+1
        
        for num in nums2:
            if num in nums1 and dict[num] != 0:
                dict[num]-=1
                li.append(num)
                
        return li
