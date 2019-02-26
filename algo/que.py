# queue = [0] * 10
# front = -1
# rear = -1
#
# rear += 1
# queue[rear] = 1
# rear += 1
# queue[rear] = 2
# rear+=1
# queue[rear] = 3
#
# while front != rear:
#     front+=1
#     print(queue[front])


# queue = [0] * 5
# front = rear = 0
#
# def isempty():
#     return front == rear
#
# def isfull():
#     return (rear+1) % len(queue) == front
#
# def enqueue(item):
#     global rear
#     if isfull():
#         print('full')
#     else:
#         rear = (rear+1) % len(queue)
#         queue[rear] = item
#
# def dequeue():
#     global front
#     if i

Queue = [0] * 1000
front = rear = -1


peopleno= 41

for who in range(1,peopleno+1):
    rear+=1
    Queue[rear] = who

while front+2!=rear :
    front+=1;    alive1 = Queue[front]
    front+= 1;    alive2 = Queue[front]
    front+= 1;    dead = Queue[front]
    rear+=1;    Queue[rear] = alive1
    rear+= 1;    Queue[rear] = alive2


print(Queue[front+1], Queue[front+2])