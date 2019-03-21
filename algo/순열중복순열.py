data=[1,2,3,4]
res=[0]*len(data)
visited=[0]*len(data)

def getsome(depth):
    if depth==len(data):
        print(res)
        return
    for i in range(len(data)):
        if not visited[i]:
            visited[i]=True
            res[depth]=data[i]
            getsome(depth+1)
            visited[i]=False
getsome(0)
print()
def getsome2(depth):
    if depth==len(data):
        print(res)
        return
    for i in range(len(data)):
        res[depth]=data[i]
        getsome2(depth+1)
getsome2(0)