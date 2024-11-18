n=int(input())
a=list(map(int,input().split()))
ts=sum(a)
ls=0
b=[]
for i in range(n):
    rs=ts-ls-a[i]
    bal=abs(ls-rs)
    b.append(bal)
    ls+=a[i]
print(' '.join(map(str,b))) 
