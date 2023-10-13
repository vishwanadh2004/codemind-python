n=int(input())
m=list(map(int,input().split()))
p=int(input())
c=0
for i in range(n):
    if m[i]==p:
        c=c+1
print(c)