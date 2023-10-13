n=int(input())
m=map(int,input().split())
s=0
p=0
for i in m:
    if i%2==0:
        s=s+i
    elif i%2!=0:
        p=p+i
diff=p-s
print(abs(diff))