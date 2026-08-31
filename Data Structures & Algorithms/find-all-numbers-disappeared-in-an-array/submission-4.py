class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        new = []
        for i in range(1,n+1):
            if i not in nums:
                new.append(i)
        return new

        