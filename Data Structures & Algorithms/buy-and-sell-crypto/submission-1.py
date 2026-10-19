class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for buy in range(len(prices)):
            sell=buy+1
            
            while sell < len(prices):
                
                if (-prices[buy] + prices[sell]) > profit:
                    profit = -prices[buy]+prices[sell]
                    
                    
                sell+=1
        return(profit)
