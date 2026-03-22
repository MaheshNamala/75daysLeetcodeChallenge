class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h={}
        for i,j in enumerate(numbers):
            diff=target-j
            if diff in h:
                return [h[diff]+1,i+1]
            h[j]=i
        return []
        