a=int(input())
b=int(input())
for i in range(a,b+1):
    d=i
    c=0
    s=0
    while(d!=0):
        rem=d%10
        d=d//10
        c+=1
        if(rem==0):
            break
        elif(i%rem==0):
            s+=1
    if(s==c):
        print(i,end=" ")