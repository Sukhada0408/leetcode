nums = ['1a','2','1a']

state = []
result = []
used = [False]*len(nums)

nums.sort()

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        state = []
        result = []
        used = [False]*len(nums)
        def permutations ():
            if len(state)==len(nums):
                result.append(state[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                state.append(nums[i])
                used[i]=True

                permutations()

                state.pop()
                used[i]=False
        permutations()
        return(result)