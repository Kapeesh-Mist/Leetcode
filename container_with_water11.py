height=list(map(int,input().split()))
m=0
i,j=0,len(height)-1
while i<j:
    m=max(m,(j-i)*min(height[i],height[j]))
    if height[i]<height[j]:
        i+=1
    else:
        j-=1
print(m)