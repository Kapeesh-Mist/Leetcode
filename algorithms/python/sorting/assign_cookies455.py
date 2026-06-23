g=list(map(int,input().split()))
s=list(map(int,input().split()))
g.sort()
s.sort()
i=j=0
n=len(g)
m=len(s)
while i<n and j<m:
    if s[j]>=g[i]:
        i+=1
    j+=1
print(i)