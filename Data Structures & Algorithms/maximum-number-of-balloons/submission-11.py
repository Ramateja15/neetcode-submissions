class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0 
        mp = {}
        for i in range(len(text)):
            if text[i] in mp:
                mp[text[i]] += 1
            else: 
                mp[text[i]] = 1
        
        isTrue = True
        while isTrue:
            for char in 'balloon':
                if char in mp:
                    mp[char] -= 1
                    if mp[char] == 0:
                        del mp[char]
                else:
                    isTrue = False
                    break

            if isTrue:
                count += 1

        return count
            

        