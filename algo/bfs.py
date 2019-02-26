data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
mymap = [[0]*8 for i in range(8)]
visited = [0] * 8
howmany = int(len(data)/2)
que = [0] * 10
front = rear = -1
distance = [-1]*10
parent = [-1]*10

def bfs(here):
    global front, rear
    rear += 1
    que[rear] = here
    visited[here] = True

    while front != rear:
        front += 1
        here = que[front]
        print(here)

        for next in range(howmany):
            if mymap[here][next] and not visited[next]:
                visited[next] = True
                distance[next] = distance[here]+1
                parent[next] = here
                rear += 1
                que[rear] = next

for i in range(8):
    start = data[i * 2]
    stop = data[i * 2 + 1]
    mymap[start][stop] = 1
    mymap[stop][start] = 1

distance[1] = 0
bfs(1)