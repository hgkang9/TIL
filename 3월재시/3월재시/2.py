import sys
sys.stdin=open('네개의구역.txt','r')


TC=int(input())
for tc in range(1,TC+1):
    print("#%d"%tc,end=' ')
    N,M=map(int,input().split())
    Mymap=[0]*N
    for n in range(N):
        Mymap[n]=list(map(int,input().split()))

    mymax = -1
    for x in range(1, M):
        for y in range(1, N):
                one = 0
                two = 0
                three = 0
                four = 0

                for ii in range(y):
                    for aa in range(x):
                        one += Mymap[ii][aa]
                    for bb in range(x,M):
                        two += Mymap[ii][bb]

                for jj in range(y, N):
                    for dd in range(x):
                        three += Mymap[jj][dd]
                    for ee in range(x,M):
                        four += Mymap[jj][ee]


                lst = [one, two, three, four]

                for i in range(4):
                    for j in range(i + 1, 4):
                        q = lst[i]
                        r = lst[j]
                        tmp = abs(q - r)
                        if tmp > mymax:
                            mymax = tmp

    print(mymax)



















