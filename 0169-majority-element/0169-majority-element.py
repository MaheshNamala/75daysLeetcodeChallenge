class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        max_count = 0
        majority = None
        
        for i in d:
            if d[i] > max_count:
                max_count = d[i]
                majority = i
        
        return majority