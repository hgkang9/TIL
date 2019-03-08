import sys
sys.stdin=open('두개의숫자열.txt','r')
T=int(input())
for tc in range(1,T+1):
    M, N = map(int, input().split())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    t=abs(N-M)+1
    ans=0
    temp=0

    for i in range(t):
        if M>=N:
            for j in range(t):
                temp=0
                tempB = [0] * j + B
                for k in range(j, j+N):
                    temp += tempB[k] * A[k]
                if temp > ans:
                    ans = temp
        else:
            for j in range(t):
                temp=0
                tempA=[0]*j + A
                for k in range(j, j+M):
                    temp += B[k] * tempA[k]
                if temp > ans:
                    ans = temp
    print('#{} {}' .format(tc, ans))