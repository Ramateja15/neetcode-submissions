class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        long = 1
        curr = 1
        if len(num) == 0:
            return 0
        for i in range(len(num)-1):
            if num[i]+1 == num[i+1]:
                curr += 1
                long = max(curr,long)
            else:
                curr = 1
        return long

        