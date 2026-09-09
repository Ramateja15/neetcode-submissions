from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        new=[]
        for key,value in sorted(count.items(), key=lambda x: (x[1], -x[0])):
            new.extend([key] * value)
        return new

