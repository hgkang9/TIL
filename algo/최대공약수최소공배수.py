def gcd(a,b):
    if b>a:
        a,b=b,a
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

x, y=map(int,input().split())
g=gcd(x,y)
l=int((x*y)/g)
print(g)
print(l)