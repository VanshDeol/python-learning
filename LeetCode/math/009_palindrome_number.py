class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        if x<0:
            return False
        rev = 0
        while x>0:
  
            rev = x %10 + rev*10
            x = x//10
     
        return original==rev

