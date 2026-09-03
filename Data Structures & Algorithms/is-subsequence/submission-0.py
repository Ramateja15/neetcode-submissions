class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cnt = 0
        for char in t:
            if cnt < len(s) and char == s[cnt]:
                cnt+= 1
        if cnt == len(s):
            return True
        return False
        