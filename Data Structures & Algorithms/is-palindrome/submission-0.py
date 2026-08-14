class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join([char for char in s if char.isalnum()])
        r_strs = "".join(reversed(strs))
        if strs.lower() == r_strs.lower():
            return True 
        return False