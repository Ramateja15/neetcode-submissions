class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0
        for word in words:
            word_count = Counter(word)
            is_valid = True
            for i,frq in word_count.items():
                if frq > char_count[i]:
                    is_valid = False
                    break
            if is_valid:
                total+= len(word)
        return total
