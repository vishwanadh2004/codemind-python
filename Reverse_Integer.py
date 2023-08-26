a=int(input())
s=0
b=a
flag=0
if a<0:
    flag=1
    b=abs(a)
while(b!=0):
    r=b%10
    b=b//10
    s=s*10+r
if flag==1:
    s=-s
print(s)