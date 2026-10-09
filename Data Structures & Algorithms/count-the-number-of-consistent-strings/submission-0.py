class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in words:
            for j in i:
                valid = True
                if j not in allowed:
                    valid = False
                    break
            if valid:
                count+= 1
        return count
                    
        