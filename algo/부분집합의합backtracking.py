data=[-1,3,-9,6,7,-6,1,5,4,-2]
visited=[0]*len(data)
sum=0
res=[0]*len(data)
def getsome(depth):
    if depth == len(data):
        return
    for i in range(len(data)):
        if not visited[i]:
            visited[i] = True
            res[depth] = data[i]
            if 
            getsome(depth + 1)
            visited[i] = False

getsome(0)