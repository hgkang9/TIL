import sys
sys.stdin=open('숫자추가.txt','r')
class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link

def Enque(item):
    global head, p
    newnode=Node(item)
    if head==None:
        head=newnode
    else:
        p=head
        while p.link:
            p=p.link
        p.link=newnode

T=int(input())
for tc in range(1,T+1):
    N, M, L=map(int, input().split())
    dataa=list(map(int, input().split()))
    plus=[[0]*2 for _ in range(M)]
    node=[]
    for i in range(M):
        plus[i]=list(map(int, input().split()))

    head=None
    for i in dataa:
        Enque(i)
    for i in range(M):
        node.append(Node(plus[i][1]))

    p=head
    count=-1
    pl=0
    while p:
        if pl>=M:
            break
        if plus[pl][0] == 0:
            node[pl].link = p
            head = node[pl]
            count = -1
            pl += 1
            p = head
        elif count+2==plus[pl][0]:
            node[pl].link=p.link
            p.link=node[pl]
            count=-1
            pl+=1
            p=head
        else:
            count+=1
            p=p.link

    p = head
    count=0
    while p:
        if count==L:
            print('#%d %d' %(tc, p.data))
            break
        p = p.link
        count+=1