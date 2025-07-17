class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Two pointer approach
        s = s.lower()
        left = 0
        right = len(s)-1

        while left < right :
            if (s[left].isalnum() and s[right].isalnum()):
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
                
            
            elif (s[left].isalnum() and not s[right].isalnum()):
                right -=1

            elif ( not s[left].isalnum() and  s[right].isalnum()):
                left +=1

            else:
                left += 1
                right -= 1
            
        return True
        ''' creating a another string with only alphanumeric
        k = s.lower()
        j = ""
        
        for i in k:
            if i.isalnum():
                j += i
      
        return j==j[::-1]
        '''
