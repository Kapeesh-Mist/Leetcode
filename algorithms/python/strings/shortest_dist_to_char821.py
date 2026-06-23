from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s=list(s)
        ans=[]
        for _ in range(len(s)):
            i,j=_,_
            while 1:
                if s[j]==c:
                    ans.append(j-_)
                    break
                if s[i]==c:
                    ans.append(_-i)
                    break
                j+=1
                i-=1
                if i<0:
                    i=0
                if j>len(s)-1:
                    j=len(s)-1
        return ans