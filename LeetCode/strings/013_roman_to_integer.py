"""
LeetCode 013 – Roman To Integer
Difficulty: Easy
Topic: Strings
Approach: Hash Map + Right-to-Left Greedy Traversal
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman= {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        prev = 0
        output = 0

        for char in reversed(s):
            value = roman[char]
            if value < prev:
                output -= value
            else:
                output += value
            prev = value
        return output  

        # output = 0
        # for i in range(len(s)-1 , -1 , -1):
        #     if i > 0 :
        #         if (s[i] == 'V' or s[i] == 'X') and s[i-1] == 'I':
        #             output += -2*(1)
                    
        #         if (s[i] == 'L' or s[i] == 'C') and s[i-1] == 'X':
        #             output += -2*(10)
                    
        #         if (s[i] == 'D' or s[i] == 'M') and s[i-1] == 'C':
        #             output += -2*(100)
        #     output += roman[s[i]]
        # return output
