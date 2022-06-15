# easy python solution
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
        
# pointer solution
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return
        p1, p2 = m-1, n-1
        
        for i in range(m+n-1,-1,-1):
            if p2 < 0:
                return
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i]=nums1[p1]
                p1-=1
            else:
                nums1[i]=nums2[p2]
                p2-=1
                
            
