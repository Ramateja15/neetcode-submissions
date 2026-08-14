class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_n = "".join(sorted(s))
        t_n = "".join(sorted(t))
        if s_n == t_n :
            return True
        else:
            return False
        