class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        counter = 1
        if len(nums)<2:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] and counter<2:
                nums[k] = nums[i]
                counter+=1
                k+=1
            elif nums[i]!=nums[i-1]:
                nums[k] = nums[i]
                k+=1
                counter=1
        return k