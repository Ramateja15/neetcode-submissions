class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        l = len(s)
        sublen = -1
        for i in range(l-1):
            curr = 0 
            for j in range(l):
                if s[i] == s[j]:
                    curr = j-i-1
            sublen = max(sublen,curr)
        return sublen
        