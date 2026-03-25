class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=prices[0]
        profit=0
        for i in prices:
            min1=min(i,min1)
            profit=max(profit,i-min1)
        return profit
