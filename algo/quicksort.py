def quick(data,start,end):
    p=data[start]
    i=start
    j=end
    while i<j:
        while data[i]<=p:
            if i < end:
                i+=1
            else:
                break
        while data[j]>=p:
            if j>start:
                j-=1
            else:
                break
        if i<j:
            data[i],data[j]=data[j],data[i]
    data[start],data[j]=data[j],data[start]
    return j

def qsort(data,start,end):
    if start<end:
        s=quick(data,start, end)
        qsort(data, start, s-1)
        qsort(data,s+1,end)

data0=[3,2,4,6,9,1,8,7,5]
data1=[11,45,23,81,28,34]
data2=[11,45,22,81,23,34,99,22,17,8]
data3=[1,1,1,1,1,0,0,0,0,0]
qsort(data0,0,len(data0)-1)
qsort(data1,0,len(data1)-1)
qsort(data2,0,len(data2)-1)
qsort(data3,0,len(data3)-1)
print(data0)
print(data1)
print(data2)
print(data3)