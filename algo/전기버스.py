import sys
sys.stdin=open('전기버스.txt','r')
T=int(input())
for tc in range(1,T+1):
    K,N,M=map(int,input().split())
    data=list(map(int,input().split()))
    elec=[0]*(N+1)
    for i in range(M):
        elec[data[i]]=1
    count=0
    countf=0
    p=0
    while (p+K)<N:
        if elec[p+K]:
            p=p+K
            count+=1
        else:
            countf=0
            for i in range(1,K):
                if elec[(p+K)-i]:
                    p=(p+K)-i
                    count+=1
                    break
                else:
                    countf+=1
            if countf==K-1:
                count=0
                break
    print('#%d %d' %(tc,count))

    # K, N, M = map(int, input().split())
    # charging_stations = list(map(int, input().split()))
    # stations = [0] * (N + 1)
    # for i in range(M):
    #     stations[charging_stations[i]] = 1
    #
    # ans = now = 0
    # while (True):
    #     before = now
    #     now += K
    #     if now >= N:
    #         break
    #     if stations[now] == 1:
    #         ans += 1
    #     else:
    #         for back in range(1, K + 1):
    #             if stations[now - back] == 1:
    #                 now -= back
    #                 ans += 1
    #                 break
    #         if now == before:
    #             ans = 0
    #             break
    # print("#%d" % tc, ans)
