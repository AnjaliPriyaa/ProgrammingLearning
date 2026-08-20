class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        max_profit = 0
        minimum_price = prices[0] - lowest stock price
        FOR i from 1 to length(prices) - 1:
        current_profit = today's price - minimum_price
        profit = max(profit, cost)
        minimum = min(minimum, prices[i])
        RETURN profit
        """
        max_profit = 0
        minimum_price = prices[0] 
        for i in prices:
            current_profit = i - minimum_price
            max_profit = max(max_profit,current_profit)
            minimum_price = min(minimum_price,i)
        return max_profit
        
        