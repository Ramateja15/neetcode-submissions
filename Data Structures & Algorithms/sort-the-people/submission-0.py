class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = {}
        n = len(names)
        for i in range(n):
            h[heights[i]] = names[i]
        res=[]
        for i in reversed(sorted(heights)):
            res.append(h[i]) 
        return res
        