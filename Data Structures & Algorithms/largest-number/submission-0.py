class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if int(nums[j]+nums[i]) > int(nums[i]+nums[j]):
                    nums[i],nums[j] = nums[j],nums[i]
        if nums[0] == '0':
            return '0'
        return "".join(nums)
