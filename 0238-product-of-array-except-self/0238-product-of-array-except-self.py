class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [1] * n
        left = 1
        for i in range(n):
            res[i] = left
            left *= arr[i]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= arr[i]

        return res