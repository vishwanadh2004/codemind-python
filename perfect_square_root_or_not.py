a=int(input())
for i in range(1,int(a**0.5)+1):
    c=0
    if(i*i==a):
        c=1
if(c==1):
    print(True)
else:
    print(False)