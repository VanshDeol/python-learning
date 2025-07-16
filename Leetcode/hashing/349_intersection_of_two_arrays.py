class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set2 = set(nums2)
        return [x for x in set(nums1) if x  in set2]
        
