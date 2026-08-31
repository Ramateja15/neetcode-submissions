class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        h ={}
        missing = []
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        for key,value in h.items():
            if value == 2:
                missing.append(key)
                break
        for i in range(1, len(nums) + 1):
            if i not in h:
                missing.append(i)
                break
        return missing