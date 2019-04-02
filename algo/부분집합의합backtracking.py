data=[-1,3,-9,6,7,-6,1,5,4,-2]
visited=[0]*len(data)

def getsome(k,sum):
    if sum == len(data):
        for i in range(len(data)):
            if visited[i]:
                print('%d' %data[i], end=' ')
        print()
        return
    if k>=10 or sum>10:
        return
    visited[k] = True
    getsome(k+1,data[k]+sum)
    visited[k] = False
    getsome(k+1,sum)

getsome(0,0)