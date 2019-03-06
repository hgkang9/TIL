mymap = [[0]*8 for i in range(8)]
data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
visited = [0]*8
howmany = int(len(data)/2)
top = -1
stack = []


# 재귀
def dfs(here):
    print(here)
    visited[here] = True

    for next in range(8):
        if mymap[here][next] and not visited[next]:
            dfs(next)


for i in range(howmany):
    start = data[i*2]
    stop = data[i*2+1]
    mymap[start][stop] = 1
    mymap[stop][start] = 1

dfs(1)

def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    if top == -1:
        return 0
    x = stack[top]
    top -= 1
    return x

def findnext(here):
    for next in range(8):
        if mymap[here][next] and not visited[next]:
            return next

def dfs(here):
    global top
    print(here)
    visited[here] = True

    while here:
        next = findnext(here)
        if next:
            push(here)
        while next:
            here = next
            print(here)
            visited[here] = True
            next = findnext(here)
            push(here)
        here = pop()