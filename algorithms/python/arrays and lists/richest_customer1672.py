accounts=list(map(int,input().split()))
m=0
for i in accounts:
    s=sum(i)
    if m<s:
        m=s
print(m)