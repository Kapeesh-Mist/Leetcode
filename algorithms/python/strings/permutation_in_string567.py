class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n>m:
            return False
        a=[0]*26
        b=[0]*26
        for i in s1:
            a[ord(i)-ord('a')]+=1
        for i in range(m):
            if i<n:
                b[ord(s2[i])-ord('a')]+=1
            else:
                b[ord(s2[i-n])-ord('a')]-=1
                b[ord(s2[i])-ord('a')]+=1
            if a==b:
                return True
        return False