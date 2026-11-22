class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = 1
        for i in nums:
            val = val*i 
        if val == 0:
            return 0
        elif val < 0:
            return -1
        else:
            return 1 