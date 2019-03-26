# import sys
# sys.stdin=open('최소생산비용.txt','r')
#
# def prod(res):
#     global prod_sum, low
#     for i in range(N):
#         prod_sum+=data[i][res[i]]
#         if prod_sum>low:
#             return
#     if prod_sum<=low:
#         low=prod_sum
#
# def getsome(depth):
#     global N, low, prod_sum
#     if depth==N:
#         prod_sum=0
#         prod(res)
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i]=True
#             res[depth]=data2[i]
#             getsome(depth+1)
#             visited[i]=False
#
# T=int(input())
# for tc in range(1,T+1):
#     N=int(input())
#     data=[list(map(int,input().split())) for _ in range(N)]
#     visited=[0]*N
#     res=[0]*N
#     data2=[0]*N
#     low=99999999999
#     prod_sum=0
#     for i in range(N):
#         data2[i]=i
#     getsome(0)
#     print(low)

import sys
sys.stdin = open('최소생산비용.txt', 'r')

def getsome(start):
    global N, low, prod_sum
    if start == N:
        if low>prod_sum:
            low=prod_sum
        return
    if prod_sum>low:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            prod_sum+=data[start][i]
            getsome(start+1)
            visited[i] = False
            prod_sum-=data[start][i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    low = 99999999999
    prod_sum = 0

    getsome(0)
    print(low)
