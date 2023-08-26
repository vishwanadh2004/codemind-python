a=int(input())
b=a*a
sm=0
while(b!=0):
    r=b%10
    b=b//10
    sm=sm+r
        
if sm==a:
    print("Neon Number")
else:
    print("Not Neon Number")