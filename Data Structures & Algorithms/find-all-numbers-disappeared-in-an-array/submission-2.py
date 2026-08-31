class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)          # Record original length
        num_set = set(nums)    # O(1) lookups
        missing = []
        
        for i in range(1, n + 1):
            if i not in num_set:
                missing.append(i)
                
        return missing

        