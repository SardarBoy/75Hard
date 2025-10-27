class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def merge(l,mid,h):
            left=N[l:mid+1]
            right=N[mid+1:h+1]
            i=j=0
            k=l
            while i <len(left) and j<len(right):
                if left[i]<=right[j]:
                    N[k]=left[i]
                    i+=1
                else:
                    N[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                N[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                N[k]=right[j]
                j+=1
                k+=1

        def mergesort(l, h):
            if l<h:
                mid=(l+h)//2
                mergesort(l,mid)
                mergesort(mid+1,h)
                merge(l,mid,h)

        mergesort(0,len(N)-1)
        return N
		
