class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i,j in enumerate((nums)):
            if j in dic and abs(i -dic[j]) <= k:
                return True
            else:
                dic[j]=i
        return False
