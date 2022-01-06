from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_idx = diff = 0
        for i, price in enumerate(prices):
            if price < prices[min_idx]:
                min_idx = i
            if price - prices[min_idx] > diff:
                diff = price - prices[min_idx]
        return diff
