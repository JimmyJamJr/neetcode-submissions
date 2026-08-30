class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0
        for i, price in enumerate(prices[1:]):
            profit = price - min_price
            best = max(profit, best)
            min_price = min(price, min_price)
        return best

            
            