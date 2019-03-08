import sys
sys.stdin=open('압축.txt','r')
T=int(input())
for tc in range(1, T+1):
    N = int(input())
    data=[[0 for _ in range(2)] for _ in range(N)]
    temp=[]
    sum2=0
    h=0
    for i in range(N):
        data[i]=list(map(str, input().split()))
    for i in range(N):
        sum2+=int(data[i][1])
        h=sum2//10 + 1
    doc=[[0]*10 for _ in range(h)]
    for i in range(N):
        for j in range(int(data[i][1])):
            temp.append(data[i][0])
    # print('#{}' .format(tc))
    # for i in range(len(temp)):
    #     print(temp[i], end='')
    #     if i%10==9:
    #         print()
    # print()
    for y in range(h):
        for x in range(10):
            a = temp.pop(0)
            doc[y][x] = a
            if not temp:
                break
    print('#%d' %tc)
    for y in range(h):
        for x in range(10):
            if doc[y][x]:
                print(doc[y][x], end='')
        print()
