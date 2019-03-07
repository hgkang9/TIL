data = [1,2,3]
n=2
visited=[0]*len(data)
temp=[]
def getsome(now, count):
    global n
    visited[now]=1
    if count<n and visited[now]:
        temp.append(data[now])

    if len(temp)==n:
        print(temp)
        return
    if now+1 > n:
        return

    visited[now]=1
    getsome(now+1, count+1)
    visited[now]=0
    getsome(now+1,count)

getsome(0,0)

