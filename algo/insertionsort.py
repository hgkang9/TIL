data=[1,9,3,6,7,0,4,9,5,5]
key=0
for i in range(1,len(data)):
    key=data[i]
    j=i-1
    while j>=0 and data[j]>key:
        data[j+1]=data[j]
        j=j-1
    data[j+1]=key
print(data)