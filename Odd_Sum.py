n=int(input())
num=list(map(int,input().split()))
sm=0
for i in num:
    if i%2!=0:
        sm=sm+i
print(sm)