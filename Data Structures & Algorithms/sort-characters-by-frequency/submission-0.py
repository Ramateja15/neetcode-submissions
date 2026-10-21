class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        h = defaultdict(list)
        for key,freq in count.items():
            h[freq].append(key)
        res = []
        for i in range(len(s),0,-1):
            if i in h:
                for c in h[i]:
                    res.append(c*i)
        return "".join(res)

        