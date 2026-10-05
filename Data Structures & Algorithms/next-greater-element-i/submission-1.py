from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        grt = {}
        for i in range(len(nums2)):
            one = nums2[i]
            for j in range(i+1,len(nums2)):
                two = nums2[j]
                if two > one:
                    grt[one] = two
                    break
            else:        
                grt[one] = -1
        return [grt[num]for num in nums1]        
                