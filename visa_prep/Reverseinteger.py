n=int(input())
sign=-1 if n<0 else 1
rev=int(str(abs(n))[::-1])*sign
if -2**31 <= rev <= 2**31-1:
    print(rev)
else:
    print(0)
