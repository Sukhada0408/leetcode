class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        days = len(prices)
        min_price = prices[0]

        for i in range(1,days):
            profit = max(profit, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        if profit<=0:
            return 0
        return profit