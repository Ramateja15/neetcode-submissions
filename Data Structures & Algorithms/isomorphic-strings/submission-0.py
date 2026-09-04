class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def pattern(str):
            lst = []
            seen = {}
            cnt  = 0 
            for ch in str:
                if ch not in seen:
                    seen[ch] = cnt
                    cnt+= 1
                lst.append(seen[ch])
            return lst
        if pattern(s) == pattern(t):
            return True
        return False
        