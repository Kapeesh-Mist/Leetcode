nums=list(map(int,input().split()))
n=m=0
for i in nums:
    if i>0:
        n+=1
    elif i<0:
        m+=1
print(m if m >= n else n)