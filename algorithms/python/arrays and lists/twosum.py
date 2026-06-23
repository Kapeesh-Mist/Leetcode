n=list(map(int.input().split()))
k=int(input())
for i in range(len(k)):
  for j in range(i+1,len(k)):
    if n[i]+n[j]==k:
      print("found")
      exit()
print("Not Found")
