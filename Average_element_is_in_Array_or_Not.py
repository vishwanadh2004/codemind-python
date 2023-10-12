n=int(input())
num=list(map(int,input().split()))
sm=0
for i in num:
    sm=sm+i
    
m=sm//n
print(m in num)