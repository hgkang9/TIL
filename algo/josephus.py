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

# while :



head=None
for i in range(1,42):
    Enque(i)

p=head
while p.link:
    print(p.data)
    p=p.link
p.link = head  # 원형연결리스트 만들기 위해