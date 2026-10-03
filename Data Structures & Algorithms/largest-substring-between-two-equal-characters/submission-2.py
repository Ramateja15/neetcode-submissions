class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mp = {}
        sublen = -1
        for i,c in enumerate(s):
            if c in mp:
                sublen = max(sublen,i-mp[c]-1)
            else:
                mp[c] = i
        return sublen        
        