import sys
sys.stdin=open('이진탐색.txt','r')
def bi_sear(data,l,r,search):
    global B_len,cnt,p,M
    mid=(l+r)//2
    if data[mid]==search:
        if p!=0:
            cnt+=1
        return
    if search>data[mid]:
        l=mid+1
        if p==1:
            return
        p=1
        return bi_sear(data,l,r,search)
    elif search<data[mid]:
        r=mid-1
        if p==-1:
            return
        p=-1
        return bi_sear(data,l,r,search)

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    B_len=len(B)
    cnt=0
    p=0
    A.sort()
    for i in range(len(B)):
        if B[i] in A:
            p=2
            bi_sear(A,0,N-1,B[i])
    print('#%d %d' %(tc,cnt))
