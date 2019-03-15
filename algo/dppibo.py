fibo=[-1]*101
fibo[0]=0
fibo[1]=1

#DP
for now in range(2,101):
    fibo[now]=fibo[now-1]+fibo[now-2]
print(fibo[100])

#memoi
def getsome(num):
    #basecase
    # return getsome(num-1)+getsome(num-2)

    if fibo[num]==-1:
        fibo[num]=getsome(num-1)+getsome(num-2)
        return fibo[num]
    else:
        return fibo[num]

print(getsome(100))