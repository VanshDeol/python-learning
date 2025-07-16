from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #Better Time and Space complexity
        return len(nums) != len(set(nums))

    '''  
        for key , value in Counter(nums).items():
            if value >= 2:
                return True
        return False
    '''
