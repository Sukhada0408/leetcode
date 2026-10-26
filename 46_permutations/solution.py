class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        state = []
        result = []
        used = [False]*len(nums)

        def permutations():
            if len(state)==len(nums):
                result.append(state[:])
                return
            for i in range(len(nums)):
                if used[i]==True:
                    continue
                state.append(nums[i])
                used[i]=True
                permutations()
                state.pop()
                used[i]=False
        permutations()
        return result