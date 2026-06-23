prices=list(map(int,input().split()))
i=0
j=1
m=0
while j<len(prices) :
    if prices[i]>prices[j]:
        i,j=j,j+1
    else:
        if prices[j]-prices[i] >m:
            m=prices[j]-prices[i]
        j+=1
print(m)