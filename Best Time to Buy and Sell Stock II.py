#state machine dp
def maxProfit(prices):
        cur_hold, cur_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        return cur_not_hold
#greedy
def maxProfit(prices):
        profit_from_price_gain = 0
        for idx in range( len(prices)-1 ):
            
            if prices[idx] < prices[idx+1]:
                profit_from_price_gain += ( prices[idx+1] - prices[idx])
                
        return profit_from_price_gain
