a=int(input())
sm=0
for i in range(1,a):
    if(a%i==0):
        sm=sm+i
    
if(sm==a):
    print("True")
else:
    print("False")
    