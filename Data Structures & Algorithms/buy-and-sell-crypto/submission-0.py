class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0          # buy day
        right = 1         # sell day
        profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                dayGain = prices[right] - prices[left]
                profit = max(profit, dayGain)
            else:
                # update right and left to find better profit
                left = right

            right += 1

        return profit