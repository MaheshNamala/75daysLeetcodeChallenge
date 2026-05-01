class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_count = {0: 1}

        for num in nums:
            current_sum += num
            
            # Check if there is a prefix sum we can subtract
            if current_sum - k in prefix_count:
                count += prefix_count[current_sum - k]
            
            # Update the hashmap
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return count