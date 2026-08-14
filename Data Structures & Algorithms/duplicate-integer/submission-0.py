class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d_lst = len(set(nums))
        nums = len(nums)
        if d_lst == nums:
            return False
        else:
            return True

        