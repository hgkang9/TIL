N=5
M=3

data = ['a','b','c','d','e']
index_fuel=[1]*N #중복일때 [M]*N
A=[0]*M

def go(now_index):
    global N,M
    if now_index==M:
        print(A)
        return
    for i in range(N):
        if index_fuel[i]>0:
            # if now_index>0:
                # if A[now_index-1]>i:
                    # continue
        index_fuel[i]=index_fuel[i]-1
        A[now_index]=i
        go(now_index+1)
        index_fuel[i] = index_fuel[i] + 1

go(0)