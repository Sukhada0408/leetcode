class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a = cost[0]
        b = cost[1]

        for i in range(2, len(cost)):
            price = cost[i]+min(a,b)
            a = b
            b = price
        return(min(a,b))