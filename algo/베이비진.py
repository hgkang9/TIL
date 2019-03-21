import sys
sys.stdin=open('베이비진.txt','r')
T=int(input())
for tc in range(1,T+1):
    data=list(map(int, input().split()))
    p1=[]
    p2=[]
    ans=0
    for i in range(12):
        if not i%2:
            p1.append(data[i])
            p1.sort()
            if len(p1)>=3:
                for j in range(2,len(p1)):
                    if p1[j-2]==p1[j-1]==p1[j] and ans==0:
                        ans=1
                        break
                    elif p1[j]-p1[j-1]==1 and ans==0:
                        if p1[j-1]-p1[j-2] == 1:
                            ans=1
                            break
                        elif p1[j-1]==p1[j-2]:
                            while p1[j-1]==p1[j-2]:
                                j-=1
                            if p1[j-1]-p1[j-2] == 1:
                                ans = 1
                                break

        else:
            p2.append(data[i])
            p2.sort()
            if len(p2)>=3:
                for k in range(2,len(p2)):
                    if p2[k-2]==p2[k-1]==p2[k] and ans==0:
                        ans=2
                        break
                    elif p2[k]-p2[k-1]==1 and ans==0:
                        if p2[k-1]-p2[k-2] == 1:
                            ans=2
                            break
                        elif p2[k-1]==p2[k-2]:
                            while p2[k-1]==p2[k-2]:
                                k-=1
                            if p2[k-1]-p2[k-2] == 1:
                                ans=2
                                break
    print('#{} {}' .format(tc,ans))
