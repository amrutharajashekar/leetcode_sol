class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        result = 0 
        i = 0
        n = len(prices) - 1
        
        while i < n : 
            while i < n and prices[i+1] <= prices[i]:
                i += 1
            buy = prices[i]
            
            while i < n and prices[i+1] > prices[i]:
                i += 1
            sell = prices[i]
            
            result += sell - buy 
        return result 
    
    
    
    """
    brief summary : we buy when the prices are down and sell them immediately next to the highest price 
    
    A + B > C 
    
    
                        *
        *
    *          
                *
    """
