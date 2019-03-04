data = 'algorithm'
l=[]
for i in data:
    l.append(i)
rep = len(l)//2

# for i in range(rep):
#     l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]
#
# new_s = ''.join(l)
# print(new_s)

start = 0
end = len(data)-1

while start<end:
    l[start], l[end] = l[end], l[start]
    start+=1
    end-=1
print(''.join(l))