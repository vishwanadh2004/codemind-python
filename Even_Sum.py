n=int(input())
m=list(map(int,input().split()))
b=0
for i in m:
    if i%2==0:
        b=b+i
print(b)
