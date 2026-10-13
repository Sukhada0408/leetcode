class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        length = len(nums)
        if target<=nums[0]:
            return 0
        for i in range(length-1):
            if nums[i]==target:
                return i
            elif nums[i+1]>=target:
                return i+1
        return length