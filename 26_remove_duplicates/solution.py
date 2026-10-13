class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[unique]=nums[i]
                unique+=1
        return unique