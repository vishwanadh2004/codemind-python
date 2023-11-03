r,c=map(int,input().split())
mat=[]
for i in range(r):
    d=list(map(int,input().split()))
    mat.append(d)
s=0
for d in mat:
    for e in d:
        s+=e
print(s)