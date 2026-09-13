class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp ={}
        n = len(nums)
        for i in nums:
            if i in mp:
                mp[i]+= 1
            else:
                mp[i] = 1
        for key,value in mp.items():
            if value > n/2:
                return key
               