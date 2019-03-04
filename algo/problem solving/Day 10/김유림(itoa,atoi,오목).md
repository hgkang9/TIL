## 1. atoi

```python
# A의 아스키 코드 :  65
# 16진수에서,  10=A, 11=B, 12=C, 13=D, 14=E, 15=F

number = ['4', '2', 'F', 'B']
count = len(number)

for i in range(count):     # for i in number 로 바로 하거나...
    if '0' <= number[i] <= '9':   # 문자도 부등호가 된다고 한다. 대박...
        number[i] = ord(number[i])-ord('0')
    else:
        number[i] =ord(number[i]) -  ord('A') + 10

print(number)
```



## 2. itoa

```python
i = 1234

# 몇 번 반복할지  미리 정하기
n=0
while True:
    if i < 10**n:
        break
    n += 1   # n=4

change = ''
count =0
while count!=n:
    number = i % 10
    change = chr(ord('0') + number) + change
    i = (i - number)//10
    count  += 1

print(change)
print(type(change))
```



## 3. 오목

```python
import sys
sys.stdin = open('hw3.txt','r')

# 오목판 정보 받기
a=[[0]*29 for i in range(5)]
for i in range(19):
    a+= [[0]*5+list(map(int,input().split())) + [0]*5]

a+=[[0]*29 for i in range(5)]

# 방향키 ( 무조건 왼쪽 좌표가 필요)
dy=[0,1,-1,1]
dx=[1,0,1,1]   # 오-하-우상-오하

def badook():
    for x in range(5,25):
        for y in range(5,25):
            if a[y][x] in [1,2]:  # 흰색이나 바둑돌이면
                for i in range(4):   # 4방향에 대하여
                    if a[y][x]==a[y+4*dy[i]][x+4*dx[i]]==a[y+3*dy[i]][x+3*dx[i]]==a[y+2*dy[i]][x+2*dx[i]]==a[y+1*dy[i]][x+1*dx[i]]!=a[y+5*dy[i]][x+5*dx[i]]:
                        if a[y][x]!=a[y-1*dy[i]][x-1*dx[i]]:
                            flag = 1
                            return (flag,y,x)
    flag = 0
    return (flag, 0, 0)


if badook()[0]==1:
    print(a[badook()[1]] [badook()[2]])
    print(badook()[1]-4,badook()[2]-4)
else:
    print(0)
```



## 5. 소방차

```python
import sys
sys.stdin = open('fire.txt','r')

pump, car = map(int,sys.stdin.readline().split())

pumps = list(map(int,sys.stdin.readline().split()))
cars = list(map(int,sys.stdin.readline().split()))

total = sorted(pumps + cars)

for i in total:
    if total.count(i)==2:
        trash = total.index(i)
        total.remove(i)
        total.remove(i)


a=[[]for i in range(2*pump)]

k=pump


def odd(data):
    length=len(data)
    mini=[]
    for i in range(0,len(data),2):
        odd_sum = 0
        origin = data[::]
        del origin[i]
        for j in range(0,len(data)-1,2):
            odd_sum += origin[j+1]-origin[j]
        mini += [odd_sum]
    return min(mini)


for what in total:
    if what in pumps:
        a[k]+=[what]
        k-=1
    else:
        k+=1
        a[k] += [what]

even_sum=0
oddd=0
for part in a:
    if len(part)!=0 and len(part)%2==0:
        for i in range(0,len(part),2):
            even_sum += part[i+1]-part[i]

    elif len(part)>=3:
        oddd += odd(part)
print(even_sum+oddd)
```

