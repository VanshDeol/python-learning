"""
LeetCode – 169. majority element
Difficulty: Easy
Topic: Arrays
Approach: Boyer-Moore Voting Algorithm
"""

#from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore Voting Algorithm
        # This algorithm works in O(n) time and O(1) space.
        # It assumes that a majority element (appears more than n/2 times) is always present.
        
        count = 0
        m_element = 0  # This will eventually hold the majority element

        for i in nums:
            if count == 0:
                # When count drops to 0, choose a new candidate
                m_element = i
            if i == m_element:
                count += 1  # Same as candidate -> vote for it
            else:
                count -= 1  # Different -> cancel out one vote

        return m_element
        

        #Sorting the list and picking the middle element as it appears more than half time majority 
        #element will be in the middle 
        #nums.sort()
        #return nums[len(nums)//2]
        
        
        
        #using counter to find frequency than returning the key that appears more than half times
        '''
        c = Counter(nums)
        l = len(nums)//2
        for key , value in c.items():
            if value > l:
                return key 
        '''
