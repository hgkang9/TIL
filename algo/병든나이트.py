import sys
sys.stdin=open('병든나이트.txt','r')
T=int(input())
for tc in range(1,T+1):
    ans=0
    N, M=map(int,input().split())
    if N>=3 and M>=7:
        ans=M-2
    elif N>=3 and M<7:
        if M>=4:
            ans=4
        else:
            ans=M
    elif N==2:
        if M>=7:
            ans=4
        elif M>=5 and M<7:
            ans=3
        elif M>=3 and M<5:
            ans=2
        else:
            ans=1
    elif N==1:
        ans=1
    print(ans)