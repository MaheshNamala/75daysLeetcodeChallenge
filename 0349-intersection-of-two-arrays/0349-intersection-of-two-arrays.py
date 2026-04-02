class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1);l=[];k=set()
        for i in nums2:
            if i in s and i not in k:
                l.append(i)
                k.add(i)
        return l