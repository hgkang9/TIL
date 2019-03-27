def find_set(x):
    if x==p[x]:
        return x
    else:
        return find_set(p[x])

def union(x,y):
    p[find_set(y)]=find_set(x)

# computer=int(input())
computer=7
N=6
data=[(1, 2), (2, 3), (1, 5), (5, 2), (5, 6), (4, 7)]
# N=int(input())
# data=[0]*N
# for i in range(N):
#     data[i]=tuple(map(int,input().split()))
p=[0]*(computer+1)
rank=[0]*(computer+1)
for i in range(1,computer+1):
    p[i]=i
    rank[i]=0
for i in range(1,computer+1):
    union(data[i-1][0],data[i-1][1])
print(data)
print(p)
print(rank)