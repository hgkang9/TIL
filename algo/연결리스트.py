class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

node1.link=node2
node2.link=node3
node3.link=node4
node4.link=node5

head=node1
p=head
print(p.data)
print(p.link.data)
print(p.link.link.data)
print(p.link.link.link.data)
print(p.link.link.link.link.data)
# while p:
#     print(p.data)
#     p=p.link