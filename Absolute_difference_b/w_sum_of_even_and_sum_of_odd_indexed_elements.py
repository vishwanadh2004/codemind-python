n=int(input())
m=list(map(int,input().split()))
i=sum(m[0:n:2])
p=sum(m[1:n:2])
diff=i-p
print(abs(diff))