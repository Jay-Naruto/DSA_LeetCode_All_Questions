# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val=prices[0]
        max_p=0

        for i in range(len(prices)):
            if min_val > prices[i]:
                min_val=prices[i]
            elif prices[i] > min_val and max_p < prices[i] - min_val :
                max_p=prices[i] - min_val
                
        return max_p
             
       
# Runtime: 717 ms, faster than 94.02% of Python online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 22.6 MB, less than 33.18% of Python online submissions for Best Time to Buy and Sell Stock.
        
