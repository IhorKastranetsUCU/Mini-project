class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left_min = prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - left_min)
            left_min = min(left_min, prices[i])
        return ans