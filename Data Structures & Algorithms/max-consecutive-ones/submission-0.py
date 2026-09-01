class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        cur = 0
        for i in nums:
            if i == 1:
                cur+= 1
                count = max(cur,count)
            else:
                cur = 0
        return count
        