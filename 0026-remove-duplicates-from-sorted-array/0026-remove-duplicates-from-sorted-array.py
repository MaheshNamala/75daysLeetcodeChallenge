class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=0
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[s]:
                s+=1
                nums[s]=nums[fast]
        # print(slow,nums[:slow])
        return s+1
        