a=int(input())
rev=0
b=a
while(b!=0):
    r=b%10
    b=b//10
    rev=rev*10+r
if rev==a:
    print('True')
else:
    print('False')