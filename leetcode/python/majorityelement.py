class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums=sorted(nums)
        n=len(nums)
        return nums[n//2]
        #Order of nlogn

        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        for i,j in dic.items():
            if j>(len(nums)/2):
                return i 
        #Order of n time and space


#Boyer Moor Voting Algorithm
# majority element occurs more than half the time. 
#So any pair of non majority elements  “cancels out,” leaving the majority at the end.
#Order of n time but 1 space

        candidate=0
        count=0
        for i in nums:
            if count==0:
                candidate=i
                count=1
            elif candidate==i:
                count+=1
            else:
                count-=1

        return candidate