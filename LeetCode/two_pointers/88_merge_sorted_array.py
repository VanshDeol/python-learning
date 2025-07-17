class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """----By using slicing -> merging ->  sorting
        nums1[m:] = nums2[:]
        nums1.sort()
        """
        #Two pointers approach
        p1 = m - 1              #Points to end of valid num1
        p2 = n - 1              #Points to end of valid num2
        p = m + n - 1           #Points to end of list 
        #comparing values then putting the bigger one at p(end)
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        

