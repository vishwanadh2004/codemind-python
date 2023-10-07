a=int(input())
sm=0
pro=1
while(a!=0):
    s=a%10
    sm=sm+s
    pro=pro*s
    a=a//10

if sm==pro:
    print("Spy Number")
else:
    print("Not Spy Number")