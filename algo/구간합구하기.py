import sys
sys.stdin=open('구간합구하기.txt','r')

def update(a,b):
    where=base+a-1
    IDT[where]=b
    where>>=1
    while where:
        IDT[where]=IDT[where*2]+IDT[where*2+1]
        where>>=1

def rsq(ffrom,to):
    ffrom=ffrom+base-1
    to=to+base-1
    sum=0
    while ffrom<to:
        if ffrom&1: #ffrom이 홀수라면
            sum+=IDT[ffrom]
            ffrom+=1
        if to%2==0:
            sum+=IDT[to]
            to-=1
        ffrom>>=1
        to>>=1
    if ffrom==to:
        sum+=IDT[ffrom]
    return sum

N,M,K=map(int, input().split())
base=1
while base<N:
    base<<=1

IDT=[0]*(2*base)

for i in range(base, N+base):
    IDT[i]=int(input())

for parent in range(base-1,0,-1):
    IDT[parent]=IDT[parent*2]+IDT[parent*2+1]

for y in range(M+K):
    a,b,c=map(int, input().split())
    if a==1:
        update(b,c)
    else:
        print(rsq(b,c))