class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cheapest_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < cheapest_price:
                cheapest_price = prices[i]
            elif prices[i] - cheapest_price > max_profit:
                max_profit = prices[i] - cheapest_price
        return max_profit
        '''
        max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i < j:
                    profit = prices[j] - prices[i]
                    #print(profit)
                    if profit > max_profit :
                        max_profit = profit
        return max_profit
        '''
