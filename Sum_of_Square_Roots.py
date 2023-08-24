a,b=map(int,input().split())
sum=0
for i in range(a,b+1):
    sum=sum+i**0.5
print(f"{sum:.2f}")
    