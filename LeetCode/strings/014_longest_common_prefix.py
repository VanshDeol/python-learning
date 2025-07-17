class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c = 0
        strs.sort()
        
        min_length = min(len(strs[0]),len(strs[-1]))
        
        for i in range(min_length):
            if strs[0][i] == strs[-1][i]:
                c += 1
            else:
                break
        return strs[0][:c]

