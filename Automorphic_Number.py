a=int(input())
b=a
c=0
while(a>0):
    c+=1
    a=a//10
a=b*b
a=a%(pow(10,c))
if(b==a):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')