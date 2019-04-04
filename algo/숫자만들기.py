import sys
sys.stdin=open('숫자만들기.txt','r')

def calc(i):
    global p,p_sub
    if op[i]=='a':
        p=p+data[i+1]
    elif op[i]=='b':
        p=p-data[i+1]
    elif op[i]=='c':
        p=p*data[i+1]
    else:
        p_sub=p/data[i+1]
        p=int(p/data[i+1])

def calc_rev(i):
    global p,p_sub
    if op[i]=='a':
        p=p-data[i-1]
    elif op[i]=='b':
        p=p+data[i-1]
    elif op[i]=='c':
        p=int(p/data[i+1])
    else:
        p=int(p_sub*data[i+1])

def go(depth):
    global ma,mi,p
    if depth==len(op):
        if p>ma:
            ma=p
        elif p<mi:
            mi=p
        return

    for i in range(len(op)):
        if not visited[i]:
            visited[i]=True
            calc(i)
            go(depth+1)
            visited[i]=False
            calc_rev(i)

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    a,b,c,d=map(int,input().split())
    data=list(map(int,input().split()))
    op=[]
    while len(op)!=a+b+c+d:
        for i in range(a):
            op.append('a')
        for i in range(b):
            op.append('b')
        for i in range(c):
            op.append('c')
        for i in range(d):
            op.append('d')
    visited=[0]*len(op)
    res=[0]*len(op)
    ma=0
    mi=999999
    a=[]
    p_sub=0
    p = data[0]
    go(0)
    print('#%d %d'%(tc, ma-mi))