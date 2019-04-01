# N=10
# M=10
# data=[]
N=int(input())
M=int(input())
data=list(map(int,input().split()))
N2=N1=N
dataN=list(map(int,list(str(N))))
dataN1=list(map(int,list(str(N1))))
dataN2=list(map(int,list(str(N2))))
cnt=0
cntk=0
if M!=10:
    for k in range(len(dataN)):
        if dataN[k] in data:
            cntk+=1
            if cntk==len(dataN):
                ans=0
            else:
                while True:
                    dataN1 = list(map(int, list(str(N1))))
                    if cnt==len(dataN1):
                        N1+=1
                        break
                    cnt=0
                    for i in range(len(dataN1)):
                        cnt+=1
                        if dataN1[i] in data:
                            cnt-=1
                    N1-=1
                cnt=0
                while True:
                    dataN2 = list(map(int, list(str(N2))))
                    if cnt==len(dataN2):
                        N2-=1
                        break
                    cnt=0
                    for i in range(len(dataN2)):
                        cnt+=1
                        if dataN2[i] in data:
                            cnt-=1
                    N2+=1
                ans=min(abs(N-100),abs(100-N),len(dataN1)+(N-N1),len(dataN2)+(N2-N))
else:
    ans=0
print(ans)
# print(abs(N-100),abs(100-N),len(dataN1)+(N-N1),len(dataN2)+(N2-N))