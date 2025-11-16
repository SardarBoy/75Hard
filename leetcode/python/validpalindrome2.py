class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipl=s[l+1:r+1]
                skipr=s[l:r]
                return (skipl[::-1]==skipl or skipr[::-1]==skipr )
            l+=1
            r-=1
        return True