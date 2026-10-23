class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        for i in range(len(nums)-2):
            seen = set()
            for j in range(i+1, len(nums)):
                c = -(nums[i]+nums[j])
                if c in seen:
                    result.add(tuple(sorted((nums[i], nums[j],c))))
                seen.add(nums[j])
        return [list(a) for a in result]