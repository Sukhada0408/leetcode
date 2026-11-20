class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        state = []
        result = []
        used = [False]*length

        def combos(start, k, state):
            if len(state)==k:
                result.append(state[:])
                return
            
            for i in range(start,length):
                if used[i]:
                    continue

                state.append(nums[i])
                used[i]=True
                combos(i+1, k, state)

                state.pop()
                used[i]=False

        for k in range(length+1):
            combos(0,k,state)
        return result