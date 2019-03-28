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
            #res[depth]=data[i]
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

def charge(start):
global change,low
if start>=battery[0]:
if low>change:
low=change
return
if change>low:
return
for i in range(battery[start],0,-1):
change+=1
charge(start+i)
change-=1

T=int(input())
for tc in range(T):
battery=list(map(int,input().split()))
change=0
low=100000
charge(1)
print("#%d %d"%(tc+1,low-1))


def prim():
while Q:
if not 0 in visited:
return
low=10000000
for i in range(len(Q)):
if low>Q[i][0] and not visited[Q[i][1]]:
low=Q[i][0]
low_index=i

score,start=Q.pop(low_index)
visited[start]=1
result[start]=score

for i in range(V+1):
if not visited[i] and mymap[i][start]:
Q.append([mymap[i][start],i])

T=int(input())
for tc in range(T):
V,E=map(int,input().split())
mymap=[[0]*(V+1) for _ in range(V+1)]
for e in range(E):
A,B,C=map(int,input().split())
mymap[A][B]=C
mymap[B][A]=C

Q=[]
for i in range(V+1):
if mymap[i][0]:
Q.append([mymap[i][0],i])

visited=[0]*(V+1)
visited[0]=1
result=[0]*(V+1)
prim()
print("#%d %d"%(tc+1,sum(result)))