class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        m = 0
        if(len(prices) == 1):
            return 0
        
        for i in range(len(prices)):      
            if(prices[i] < buy):
                buy = prices[i]
            else:
                m = max(m, prices[i]-buy)
        
        return m