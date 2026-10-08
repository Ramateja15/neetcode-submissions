class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        max = 0
        for key,value in count.items():
            if value > max:
                max = value
        if count[max] == max:
            return max
        return -1