class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length-1
        while left<right:
            mid = low + (right-left//2)
            if nums[mid]==target:
                return nums
            if nums[mid]<target:
                left = mid
            if nums[mid]>target:
                right = mid
        return -1