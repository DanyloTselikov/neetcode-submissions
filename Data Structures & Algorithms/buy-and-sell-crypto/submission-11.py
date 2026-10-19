class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1 
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1
                continue
                
            if (-prices[buy] + prices[sell]) > profit :
                profit = -prices[buy]+prices[sell]
                

            sell+=1
        return(profit)