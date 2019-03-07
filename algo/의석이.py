import sys
sys.stdin=open('의석이.txt','r')
T=int(input())
for tc in range(1,T+1):
    data=[['&' for _ in range(15)] for _ in range(5)]
    res=[]
    l=0
    for y in range(5):
        data[y] = list(map(str, input()))

    for i in range(5):
        if len(data[i])>l:
            l=len(data[i])
    for i in range(5):
        if len(data[i])<l:
            for j in range(l-len(data[i])):
                data[i].append('&')

    print('#%d ' %tc, end='')
    for x in range(l):
        for y in range(5):
            res.append(data[y][x])

    for i in res:
        if i != '&':
            print(i, end='')
    print()