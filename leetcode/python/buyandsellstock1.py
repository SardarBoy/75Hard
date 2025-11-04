class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        maxx=0
        for i in range(1,len(prices)):
            if prices[i]<prices[left]:
                left=i
            maxx=max(prices[i]-prices[left],maxx)
            
            
        return maxx