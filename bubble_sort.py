n=int(input())
k=list(map(int,input().split()))
for i in range(n):
    for j in range(0,n-i-1):
        if k[j]>k[j+1]:
            k[j],k[j+1]=k[j+1],k[j]