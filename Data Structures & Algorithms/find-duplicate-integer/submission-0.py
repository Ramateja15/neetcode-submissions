class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = set()
        for i in range(len(nums)):
            if nums[i] not in n :
                n.add(nums[i])
            else :
                return nums[i]
        


    
        