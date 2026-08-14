class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        lst = []
        for i in strs:
            word = ''.join(sorted(i))
            if word in h:
                h[word].append(i)
            else:
                h[word] = [i]
        for i in h.values():
            lst.append(i)
        return lst
        