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
    min_i = T[0]
    for i in range(len(T)):
        if min_dist_value>dist[T[i]]:
            min_dist_value=dist[T[i]]
            min_i=T[i]
    T.remove(min_i)
    print(T)
    print(min_i)
    print(dist)
    for i in range(N):
        dist[i]=min(dist[i],dist[min_i]+data[min_i][i])
    print(dist)
print(dist)
