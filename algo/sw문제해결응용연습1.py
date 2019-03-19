import sys
sys.stdin=open('sw문제해결.txt','r')
a=list(map(int,input()))
l=len(a)
r=0
# for j in range(0,l,7):
#     if not j%7:
#         print(r)
#         r=0
#     for i in range(6+j,-1+j,-1):
#         if a[i]&(1<<i):
#             r+=2**i

for start in range(0,l,7):
    r=0
    for now in range(start,start+7):
        r=r*2+int(a[now])
    print(r, end=' ')
print()

for tc in range(0,l//7):
    r=0
    for now in range(tc*7, tc*7+7):
        r<<=1
        r+=int(a[now])
    print(r, end=' ')
print()

r=0
for i in range(l):
    r=r*2+int(a[i])
    if (i+1)%7==0:
        print(r,end=' ')
        r=0