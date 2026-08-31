class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)          # Record original length
        nums = set(nums)    # O(1) lookups
        missing = []
        
        for i in range(1, n + 1):
            if i not in nums:
                missing.append(i)
                
        return missing

        