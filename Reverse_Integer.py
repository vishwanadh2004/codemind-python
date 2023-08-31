a=int(input())
flag=0
rev=0
b=a
if a<0:
    flag=1
    b=abs(a)
while b!=0:
    r=b%10
    b=b//10
    rev=rev*10+r
if flag == 1:
    rev=-rev
print(rev)