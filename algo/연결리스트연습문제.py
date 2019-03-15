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

def Enpque(item):
    global head, p
    newnode = Node(item)
    if head == None:
        head = newnode
    else:
        p = head
        if p.link:
            while p.link:
                if p.link.data>newnode.data:
                    newnode.link=p.link
                    p.link=newnode
                    break
                p = p.link
        else:
            p.link = newnode

head=None
Enque(1)
Enque(5)
Enque(2)
Enque(4)
Enque(3)
p=head
while p:
    print(p.data)
    p=p.link

head=None
Enpque(1)
Enpque(5)
Enpque(2)
Enpque(4)
Enpque(3)
p=head
while p:
    print(p.data)
    p=p.link
