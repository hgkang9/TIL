data=[[0,3,4,999,999,999],
      [999,0,999,5,999,999],
      [999,1,0,4,5,999],
      [999,999,999,0,3,4],
      [3,999,999,999,0,5],
      [999,999,999,999,999,0]]
N=6
S=0
T=[1,2,3,4,5]

dist=[0]*N
for i in range(N):
    dist[i]=data[S][i]
while T:
    min_dist_value = dist[T[0]]
    minv = T[0]
    for i in range(0,len(T)):
        if min_dist_value>dist[T[i]]:
            min_dist_value=dist[T[i]]
            minv=T[i]
    T.remove(minv)
    print(T)
    print(minv)
    print(dist)
    for i in range(0,N):
        dist[i]=min(dist[i],dist[minv]+data[minv][i])
    print(dist)
print(dist)


