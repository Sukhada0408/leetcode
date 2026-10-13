class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        count = 0
        for i in range (length):
            if nums[i]!=val:
                nums[count] = nums[i]
                count += 1
        return count