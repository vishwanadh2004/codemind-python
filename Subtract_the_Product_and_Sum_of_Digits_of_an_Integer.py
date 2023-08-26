a=int(input())
sum=0
pro=1
while(a!=0):
    r=a%10
    a=a//10
    sum=sum+r
    pro=pro*r
    
sub=pro-sum
print(sub)