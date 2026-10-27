class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = [i for i in range(1,n+1)]
        state = []
        result = []
        used = [False]*n

        def combos(start, state):
            if len(state)==k:
                result.append(state[:])
                return
            for i in range(start,n):
                if used[i]:
                    continue
                
                state.append(nums[i])
                used[i]=True

                combos(i+1, state)

                state.pop()
                used[i]=False

        combos(0, state)
        return result