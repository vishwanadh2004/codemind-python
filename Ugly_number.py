a=int(input())
k=0
while(a!=1):
    if a%2==0:
        a//=2
    elif a%3==0:
        a//=3
    elif a%5==0:
        a//5
    else:
        k+=1
        break
if k!=0:
    print("Not Ugly Number")
else:
    print("Ugly Number")