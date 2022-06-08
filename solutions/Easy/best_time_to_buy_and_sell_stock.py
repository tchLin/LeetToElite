#slower 1114 ms #25.1 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_pointer=0
        sell_pointer=1
        profit=0
        li_len=len(prices)
        
        while sell_pointer < li_len:
            if prices[buy_pointer] < prices[sell_pointer]:
                profit=max(profit, prices[sell_pointer] - prices[buy_pointer])
            else:
                buy_pointer=sell_pointer
            sell_pointer+=1
        return profit
        
        
       
#faster #971 ms #25 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        li_len=len(prices)
        highest_price=prices[-1]
        highest_profit=0
        for i in range(li_len-1, -1, -1):
            if prices[i] > highest_price:
                highest_price = prices[i]
            if highest_profit < highest_price - prices[i]:
                highest_profit = highest_price - prices[i]
        return highest_profit
