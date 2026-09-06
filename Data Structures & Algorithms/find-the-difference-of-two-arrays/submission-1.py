class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        curr1= []
        curr2= []
        for i in set(nums1):
            if i not in nums2 and i not in curr1:
                curr1.append(i)
        for i in set(nums2):
            if i not in nums1 and i not in curr2:
                curr2.append(i)
        return [curr1,curr2]
            
        