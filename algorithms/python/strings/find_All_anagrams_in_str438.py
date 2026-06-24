

from git import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)
        a=[0]*26
        b=[0]*26
        r=[]
        for i in p:
            a[ord(i)-ord('a')]+=1
        for i in range(n):
            if i<m:
                b[ord(s[i])-ord('a')]+=1
            else:
                b[ord(s[i])-ord('a')]+=1
                b[ord(s[i-m])-ord('a')]-=1
            if a==b:
                r.append(i-m+1)
        return r