from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profitMade = 0
        l = 0
        r = 1

        while r < n:
            if prices[r] > prices[l]:
                profitMade += prices[r] - prices[l]   
            l = r      
            r += 1
        return profitMade
