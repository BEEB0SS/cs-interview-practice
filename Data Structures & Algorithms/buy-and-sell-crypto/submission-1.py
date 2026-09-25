class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = 0
        last = 1
        curr_max = 0
        while first != last and last < len(prices):
            profit = prices[last] - prices[first]
            if profit <= 0:
                first = last
                last += 1
            else:
                last += 1
            if profit > curr_max:
                curr_max = profit
        return curr_max


        