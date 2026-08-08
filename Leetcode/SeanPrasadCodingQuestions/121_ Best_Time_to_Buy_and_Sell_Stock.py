class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         profit = max(profit, prices[j]-prices[i])
        # return profit
        profit = 0
        buy = 0
        sell = 1
        for i in range(len(prices)-1):
            if prices[buy] > prices[sell]:
                buy=sell
            else:
                profit = max(profit, prices[sell]-prices[buy])
            sell += 1
        return profit

        
