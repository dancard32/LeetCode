class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        currentMinimumPrice = float("inf")
        for price in prices:
            if price < currentMinimumPrice:
                currentMinimumPrice = price
            if price - currentMinimumPrice > maxProfit:
                maxProfit = price - currentMinimumPrice
        return maxProfit
        
        

