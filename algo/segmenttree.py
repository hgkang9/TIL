IDT=[0]*(1<<4)
data=[9,8,5,7,2]
l=len(data)
base=1

while base<l:
    base<<=1
for now in range(base, l+base):
    IDT[now]=data.pop(0)
for parent in range(base-1,0,-1):
    IDT[parent]=IDT[parent*2]+IDT[parent*2+1]

def update(a,b):
    where=base+a-1
    IDT[where]=b
    where>>=1
    while where:
        IDT[where]=IDT[where*2]+IDT[where*2+1]
        where>>=1

def rsq(ffrom,to):
    ffrom=ffrom+base-1
    to=to+base-1
    sum=0
    while ffrom<to:
        if ffrom&1: #ffrom이 홀수라면
            sum+=IDT[ffrom]
            ffrom+=1
        if to%2==0:
            sum+=IDT[to]
            to-=1
        ffrom>>=1
        to>>=1
    if ffrom==to:
        sum+=IDT[ffrom]
    return sum

update(3,1)
print(IDT)
print(rsq(3,8))
