class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        new_idx= -1
        for idx,i in enumerate(s):
            if char_count[i] == 1:
                new_idx= idx
                break
        return new_idx