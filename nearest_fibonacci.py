a=int(input())
b=0
c=1
d=b+c
while d<=a:
    b=c
    c=d
    d=b+c
if a-c<d-a:
    print(c)
elif a-c>d-a:
    print(d)
else:
    print(c,d)