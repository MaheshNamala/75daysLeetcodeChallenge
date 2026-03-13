class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h={}
        for i in nums:
            if i in h:
                return True
            h[i]=h.get(i,0)+1
        return False
        