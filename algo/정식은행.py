import sys
sys.stdin=open('정식은행.txt', 'r')
T=int(input())

def bnc(bn):
    global bn_sum
    bn.reverse()
    for i in range(len(bn)):
        bn_sum+=bn[i]*(2**i)
    return bn_sum

def tnc(tn):
    global tn_sum
    tn.reverse()
    for i in range(len(tn)):
        tn_sum+=tn[i]*(3**i)
    return tn_sum

for tc in range(1,T+1):
    bn=list(map(int,input()))
    tn=list(map(int,input()))
    bn_sum=0
    tn_sum=0
    bn_cand=[0]*(len(bn))
    tn_cand1=[0]*(len(tn))
    tn_cand2=[0]*(len(tn))

    for i in range(len(bn_cand)):
        bn_sum=0
        if bn[i]:
            bn[i]=0
            bn_cand[i]=bnc(bn)
            bn.reverse()
            bn[i]=1
        else:
            bn[i]=1
            bn_cand[i]=bnc(bn)
            bn.reverse()
            bn[i]=0

    for i in range(len(tn_cand1)):
        tn_sum=0
        if tn[i]==1:
            tn[i]=0
            tn_cand1[i]=tnc(tn)
            tn.reverse()
            tn[i]=1

            tn_sum=0
            tn[i]=2
            tn_cand2[i] = tnc(tn)
            tn.reverse()
            tn[i]=1
        elif tn[i]==2:
            tn[i]=0
            tn_cand1[i] = tnc(tn)
            tn.reverse()
            tn[i]=2

            tn_sum=0
            tn[i]=1
            tn_cand2[i] = tnc(tn)
            tn.reverse()
            tn[i]=2
        else:
            tn[i]=1
            tn_cand1[i] = tnc(tn)
            tn.reverse()
            tn[i]=0

            tn_sum = 0
            tn[i]=2
            tn_cand2[i] = tnc(tn)
            tn.reverse()
            tn[i]=0

    ans=0
    for i in range(len(bn_cand)):
        if (bn_cand[i] in tn_cand1) or (bn_cand[i] in tn_cand2):
            ans=bn_cand[i]
            break
    print('#%d %d' %(tc, ans))