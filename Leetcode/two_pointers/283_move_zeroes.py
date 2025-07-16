class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        for i in nums[:]:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        '''
        pos  = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pos] = nums[pos] , nums[i]
                pos += 1
        
