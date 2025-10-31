class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        li=[[] for i in range(len(nums)+1)]

        for i in nums:
            dic[i]=1+dic.get(i,0)
        
        for i,j in dic.items():
            li[j].append(i)

        res=[]
        for i in range(len(nums),0,-1):
            for j in li[i] :
                res.append(j)
                if len(res)==k:
                    return res
