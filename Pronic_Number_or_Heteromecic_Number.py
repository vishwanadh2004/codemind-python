a=int(input())
b=0
for i in range(1,(a//2)+1,1):
  if i*(i+1)==a:
     b+=1 
if b!=0:
   print('YES')
else:
   print('NO')
        