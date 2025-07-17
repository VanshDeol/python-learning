from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        #calculate frequency using Counter then sort it according to frequency then convert it to dictionary
        k = dict(sorted(Counter(s).items() , key=lambda x:x[1]))

        for key , value in k.items():
            if value == 1:
                return s.index(key)
        return -1
        
        '''----Not good for large input----
        for char in s:
            if s.count(char) == 1:
                return(s.index(char))
            
        return(-1)
        '''
