class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_ele  =  n * n
        miss= []
        mp={}
        for i in grid:
            for j in i:
                if j in mp:
                    miss.append(j)
                mp[j] = 1
        for i in range(1,total_ele+1):
            if i not in mp:
                miss.append(i)
        return miss

        