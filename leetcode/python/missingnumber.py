class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        count=(n*(n+1))//2
        return (count-sum(nums))